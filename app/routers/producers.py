from fastapi import APIRouter, HTTPException
from ..models.producer import Producer
from typing import List

router = APIRouter(prefix="/producers", tags=["producers"])

items = [Producer(id=1, name="Spendrups"), Producer(id=2, name="Pripps")]

@router.get("/")
async def get_all() -> List[Producer]:
    return items

@router.get("/{id}")
async def get_by_id(id: int) -> Producer:
    for i in items:
        if i.id == id:
            return i
        
    raise HTTPException(status_code=404, detail=f"Producer with id: {id} not found.")
