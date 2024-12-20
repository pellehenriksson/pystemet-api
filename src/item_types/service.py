from sqlmodel.ext.asyncio.session import AsyncSession
from sqlmodel import select, asc

from ..db.schemas import ItemType

class ItemTypeService:
    async def get_all(self, session: AsyncSession):
        statement = select(ItemType).order_by(asc(ItemType.name))
        result = await session.exec(statement)
        return result.all()
