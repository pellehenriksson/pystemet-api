from typing import List
from fastapi import APIRouter, HTTPException, Depends
from sqlmodel.ext.asyncio.session import AsyncSession

from src.db.main import get_session
from src.suppliers.models import SupplierViewModel
from src.suppliers.service import SupplierService

router = APIRouter(prefix="/suppliers", tags=["supplier"])

service = SupplierService()

@router.get("/", response_model=List[SupplierViewModel])
async def get_all(session: AsyncSession = Depends(get_session)):
    return await service.get_all(session) 

@router.get("/{id}", response_model=SupplierViewModel)
async def get_by_id(id: int, session: AsyncSession = Depends(get_session)):

    item = await service.get_by_id(id, session)
    if item is not None: return item
            
    raise HTTPException(status_code=404, detail=f"Supplier with id: {id} not found.")
