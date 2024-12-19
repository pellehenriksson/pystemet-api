from sqlmodel.ext.asyncio.session import AsyncSession
from sqlmodel import select, asc

from ..db.schemas import Producer

class ProducerService:
    async def get_all(self, session: AsyncSession):
        statement = select(Producer).order_by(asc(Producer.name))
        result = await session.exec(statement)
        return result.all()

    async def get_by_id(self, id:int, session: AsyncSession):
        statement = select(Producer).where(Producer.id == id)
        result = await session.exec(statement)
        return result.first() or None
        
