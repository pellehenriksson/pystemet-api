from typing import List
from fastapi import APIRouter, HTTPException, Depends
from sqlmodel.ext.asyncio.session import AsyncSession

from src.db.schemas import Supplier
from src.db.main import get_session
from src.suppliers.service import SupplierService

router = APIRouter(prefix="/suppliers", tags=["supplier"])

service = SupplierService()

@router.get("/")
async def get_all(session: AsyncSession = Depends(get_session)) -> List[Supplier]:
    return await service.get_all(session) 

@router.get("/{id}")
async def get_by_id(id: int, session: AsyncSession = Depends(get_session)) -> Supplier:

    item = await service.get_by_id(id, session)
    if item is not None: return item
            
    raise HTTPException(status_code=404, detail=f"Supplier with id: {id} not found.")
