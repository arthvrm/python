from fastapi import FastAPI, HTTPException
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship, DeclarativeBase, Mapped, mapped_column

# Підключення до бд PostgreSQL
DATABASE_URL = "postgresql://postgres:password13@127.0.0.1/for_fastapi1"
engine = create_engine(DATABASE_URL, echo=True)

# Створення базового класу для оголошень моделі SQLAlchemy
class Base(DeclarativeBase):
    pass

# Оголошення моделі користувача
class User(Base):
    __tablename__ = "users"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String)
    
    records: Mapped[String["Record"]] = relationship(back_populates="user", cascade="all, delete")
    
    def __repr__(self) -> str:
        return f"User(id={self.id!r}, name={self.name!r})"


class Record(Base):
    __tablename__ = "records"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    record: Mapped[str] = mapped_column(String)
    
    user: Mapped["User"] = relationship(back_populates="records")
    
    def __repr__(self) -> str:
        return f"Record(id={self.id!r}, record={self.record!r})"


Base.metadata.create_all(bind=engine)


SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


app = FastAPI()


@app.post("/users/")
def create_user(name: str) -> object:
    db = SessionLocal()
    user = User(name=name)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user


@app.get("/users/{user_id}")
def read_user(user_id: int) -> object:
    db = SessionLocal()
    user = db.query(User).filter(User.id == user_id).first()
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user


@app.put("/users/{user_id}")
def update_user(user_id: int, name: str):
    db = SessionLocal()
    user = db.query(User).filter(User.id == user_id).first()
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    user.name = name
    db.commit()
    db.refresh(user)
    return user


@app.delete("/users/{user_id}")
def delete_user(user_id: int) -> object:
    db = SessionLocal()
    user = db.query(User).filter(User.id == user_id).first()
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    db.delete(user)
    db.commit()
    return {"message": "User deleted successfully"}