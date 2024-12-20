from typing import List
from fastapi import APIRouter, Depends
from sqlmodel.ext.asyncio.session import AsyncSession

from src.db.main import get_session
from src.item_styles.models import ItemStyleViewModel
from src.item_styles.service import ItemStyleService

router = APIRouter(prefix="/item-styles", tags=["item-styles"])

service = ItemStyleService()

@router.get("/", response_model=List[ItemStyleViewModel])
async def get_all(session: AsyncSession = Depends(get_session)):
    return await service.get_all(session) 