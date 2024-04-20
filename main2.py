from fastapi import FastAPI

app = FastAPI()


board = (['rw', 'kw', 'bw', 'qw', 'Kw', 'bw', 'kw', 'rw'],
         ['pw', 'pw', 'pw', 'pw', 'pw', 'pw', 'pw', 'pw'],
         ['  ', '  ', '  ', '  ', '  ', '  ', '  ', '  '],
         ['  ', '  ', '  ', '  ', '  ', '  ', '  ', '  '],
         ['  ', '  ', '  ', '  ', '  ', '  ', '  ', '  '],
         ['  ', '  ', '  ', '  ', '  ', '  ', '  ', '  '],
         ['pb', 'pb', 'pb', 'pb', 'pb', 'pb', 'pb', 'pb'],
         ['rb', 'kb', 'bb', 'qb', 'Kb', 'bb', 'kb', 'rb'])


def show_board() -> None:
    for i in range(7, -1, -1):
        print(board[i])


def valid_colors(player: str = None, move_from: tuple = None, move_to: tuple = None) -> object:
    p_color = player[0].lower()
    chosen_piece = board[move_from[1]][move_from[0]]
    target_piece = board[move_to[1]][move_to[0]]
    if p_color == chosen_piece[1]:
        print(p_color, "correctly chosen piece", move_from, chosen_piece)
        if target_piece[1] is not p_color:
            print(p_color, "correctly chosen enemy piece", move_to, target_piece)
        else:
            print(p_color, "wrongly chosen enemy piece", move_to, target_piece)
            return exit()
    else:
        print(p_color, "wrongly chosen piece", move_from, chosen_piece)
        return exit()


def what_piece(move_from: tuple = None, move_to: tuple = None) -> object:
    chosen_piece = board[move_from[1]][move_from[0]]
    if chosen_piece[0] == 'K': return king(move_from=move_from, move_to=move_to)
    elif chosen_piece[0] == 'q': return queen(move_from=move_from, move_to=move_to)
    elif chosen_piece[0] == 'b': return bishop(move_from=move_from, move_to=move_to)
    elif chosen_piece[0] == 'k': return knight(move_from=move_from, move_to=move_to)
    elif chosen_piece[0] == 'r': return rook(move_from=move_from, move_to=move_to)
    elif chosen_piece[0] == 'p': return pawn(move_from=move_from, move_to=move_to)
    else: pass


def king(move_from: tuple = None, move_to: tuple = None) -> object:
    steps_x = move_to[0] - move_from[0]
    steps_y = move_to[1] - move_from[1]
    if abs(steps_x) > 1 or abs(steps_y) > 1:
        print("not normal steps king (", steps_x, steps_y, ')')
        return exit()
    else:
        print("normal steps king (", steps_x, steps_y, ')')
        board[move_to[1]][move_to[0]] = board[move_from[1]][move_from[0]]
        board[move_from[1]][move_from[0]] = '  '


def queen(move_from: tuple = None, move_to: tuple = None) -> object:
    steps_x = move_to[0] - move_from[0]
    steps_y = move_to[1] - move_from[1]
    if abs(steps_x) == abs(steps_y):
        print("normal steps queen (", steps_x, steps_y, ')')
    elif abs(steps_x) == 0 or abs(steps_y) == 0:
        print("normal steps queen (", steps_x, steps_y, ')')
    else:
        print("not normal steps queen (", steps_x, steps_y, ')')
        return exit()
    board[move_to[1]][move_to[0]] = board[move_from[1]][move_from[0]]
    board[move_from[1]][move_from[0]] = '  '


def bishop(move_from: tuple = None, move_to: tuple = None) -> object:
    steps_x = move_to[0] - move_from[0]
    steps_y = move_to[1] - move_from[1]
    if abs(steps_x) == abs(steps_y):
        print("normal steps queen (", steps_x, steps_y, ')')
    else:
        print("not normal steps queen (", steps_x, steps_y, ')')
        return exit()
    board[move_to[1]][move_to[0]] = board[move_from[1]][move_from[0]]
    board[move_from[1]][move_from[0]] = '  '


def knight(move_from: tuple = None, move_to: tuple = None) -> object:
    steps_x = move_to[0] - move_from[0]
    steps_y = move_to[1] - move_from[1]
    if abs(steps_x) > 2 or abs(steps_y) > 2:
        print("not normal steps knight (", steps_x, steps_y, ')')
        return exit()
    elif abs(steps_x) < 1 or abs(steps_y) < 1:
        print("not normal steps knight (", steps_x, steps_y, ')')
        return exit()
    elif abs(abs(steps_x) - abs(steps_y)) == 1:
        print("normal steps knight (", steps_x, steps_y, ')')
    else:
        print("not normal steps knight (", steps_x, steps_y, ')')
        return exit()
    board[move_to[1]][move_to[0]] = board[move_from[1]][move_from[0]]
    board[move_from[1]][move_from[0]] = '  '


def rook(move_from: tuple = None, move_to: tuple = None) -> object:
    steps_x = move_to[0] - move_from[0]
    steps_y = move_to[1] - move_from[1]
    if abs(steps_x) == 0 or abs(steps_y) == 0:
        print("normal steps queen (", steps_x, steps_y, ')')
    else:
        print("not normal steps queen (", steps_x, steps_y, ')')
        return exit()
    board[move_to[1]][move_to[0]] = board[move_from[1]][move_from[0]]
    board[move_from[1]][move_from[0]] = '  '


def pawn(move_from: tuple = None, move_to: tuple = None) -> object:
    target_piece = board[move_to[1]][move_to[0]]
    steps_x = move_to[0] - move_from[0]
    steps_y = move_to[1] - move_from[1]
    if abs(steps_x) == 0 and abs(steps_y) < 2:
        print("normal steps pawn (", steps_x, steps_y, ')')
    if abs(steps_y) == 1 and abs(steps_y) < 2 and target_piece == '  ':
        print("normal steps pawn (", steps_x, steps_y, ')')
    else:
        print("not normal steps pawn (", steps_x, steps_y, ')')
        return exit()
    board[move_to[1]][move_to[0]] = board[move_from[1]][move_from[0]]
    board[move_from[1]][move_from[0]] = '  '


def move(player: str = None, move_from: tuple = None, move_to: tuple = None) -> None:
    valid_colors(player= player, move_from=move_from, move_to=move_to)
    what_piece(move_from=move_from, move_to=move_to)


@app.get("/start")
def start_game():
    show_board()
    loop = True
    while loop:
        color = input("enter color:")
        if color == "exit":
            return exit()
        mfx = int(input("enter move from x:"))
        mfy = int(input("enter move from y:"))
        mtx = int(input("enter move to x:"))
        mty = int(input("enter move to y:"))
        move(player=color, move_from=(mfx, mfy), move_to=(mtx, mty))
        show_board()