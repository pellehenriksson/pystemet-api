from sqlmodel import create_engine, text, SQLModel
from sqlalchemy import URL
from sqlalchemy.ext.asyncio import AsyncEngine
#from ..config import Config

engine = AsyncEngine(create_engine(url="postgresql+asyncpg://postgres:pelle666@localhost/pystemet", echo=True))

async def init_db():
    async with engine.begin() as connection:
        from ..models.producer import Producer

        await connection.run_sync(SQLModel.metadata.create_all)

        #sql = text("SELECT 'Hello SQL'")
        #result = await connection.execute(sql)
        #print(result.all())