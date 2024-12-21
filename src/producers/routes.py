from typing import List
from fastapi import APIRouter, HTTPException, Depends
from sqlmodel.ext.asyncio.session import AsyncSession

from src.db.main import get_session
from src.producers.models import ProducerViewModel
from src.producers.service import ProducerService

router = APIRouter(prefix="/producers", tags=["producers"])

service = ProducerService()

@router.get("/", response_model=List[ProducerViewModel])
async def get_all(session: AsyncSession = Depends(get_session)):
    return await service.get_all(session) 

@router.get("/{id}", response_model=ProducerViewModel)
async def get_by_id(id: int, session: AsyncSession = Depends(get_session)):

    item = await service.get_by_id(id, session)
    if item is not None: return item
            
    raise HTTPException(status_code=404, detail=f"Producer with id: {id} not found.")
