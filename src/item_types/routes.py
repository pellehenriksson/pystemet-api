from typing import List
from fastapi import APIRouter, Depends
from sqlmodel.ext.asyncio.session import AsyncSession

from src.db.main import get_session
from src.item_types.models import ItemTypeViewModel
from src.item_types.service import ItemTypeService

router = APIRouter(prefix="/item-types", tags=["item-types"])

service = ItemTypeService()

@router.get("/", response_model=List[ItemTypeViewModel]) # response model seems to be mapping??
async def get_all(session: AsyncSession = Depends(get_session)):
    return await service.get_all(session) 
