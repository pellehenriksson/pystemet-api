from fastapi import APIRouter, HTTPException
from ..models.producer import Producer

router = APIRouter(prefix="/producers", tags=["producers"])

items = [Producer(id=1, name="Spendrups"), Producer(id=2, name="Pripps")]

@router.get("/")
async def read_producers() -> list[Producer]:
    return items

@router.get("/{id}")
async def read_producer(id: int) -> Producer:
    for i in items:
        if i.id == id:
            return i
    raise HTTPException(status_code=404, detail=f"Producer with id: {id} not found.")
