from typing import List
from fastapi import APIRouter, Depends
from sqlmodel.ext.asyncio.session import AsyncSession

from src.db.schemas import ItemType
from src.db.main import get_session
from src.item_types.service import ItemTypeService

router = APIRouter(prefix="/item-types", tags=["item-types"])

service = ItemTypeService()

@router.get("/")
async def get_all(session: AsyncSession = Depends(get_session)) -> List[ItemType]:
    return await service.get_all(session) 