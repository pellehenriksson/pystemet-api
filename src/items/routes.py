from typing import List
from fastapi import APIRouter, HTTPException, Depends
from sqlmodel.ext.asyncio.session import AsyncSession

from src.db.main import get_session

router = APIRouter(prefix="/items", tags=["items"])