from sqlmodel.ext.asyncio.session import AsyncSession
from sqlmodel import select, asc

from ..db.schemas import ItemStyle

class ItemStyleService:
    async def get_all(self, session: AsyncSession):
        statement = select(ItemStyle).order_by(asc(ItemStyle.name))
        result = await session.exec(statement)
        return result.all()