from sqlmodel.ext.asyncio.session import AsyncSession
from sqlmodel import select, asc

from ..db.schemas import Supplier

class SupplierService:
    async def get_all(self, session: AsyncSession):
        statement = select(Supplier).order_by(asc(Supplier.name))
        result = await session.exec(statement)
        return result.all()

    async def get_by_id(self, id:int, session: AsyncSession):
        statement = select(Supplier).where(Supplier.id == id)
        result = await session.exec(statement)
        return result.first() or None