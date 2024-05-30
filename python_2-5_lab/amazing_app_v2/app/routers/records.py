from app import schemes, crud
from app.database import get_db

from fastapi import APIRouter, Depends, HTTPException

from sqlalchemy.orm import Session

records_router = APIRouter(prefix="/records", tags=["records"])
