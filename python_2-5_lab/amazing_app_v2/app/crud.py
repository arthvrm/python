from typing import Optional

from app import models
from app import schemes

from sqlalchemy.orm import Session

import hashlib


def create_user(db: Session, user: schemes.UserCreate) -> schemes.User:
    db_user = models.User(email=user.email, first_name=user.first_name,
                          second_name=user.second_name, password=user.password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def create_user_record(db: Session, item: schemes.RecordCreate, user_id: int) -> schemes.Record:
    db_record = models.Record(**item.dict(), user_id=user_id)
    db.add(db_record)
    db.commit()
    db.refresh(db_record)
    return db_record


def update_user(db: Session, user: schemes.UserCreate) -> schemes.Record:
    db_user = db.query(models.User).filter(models.User.email == user.email).first()
    db_user.first_name = user.first_name
    db_user.second_name = user.second_name
    db_user.email = user.email
    db.commit()
    return db_user


def get_user_by_email(db: Session, email: str) -> Optional[models.User]:
    return db.query(models.User).filter(models.User.email == email).first()


def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()