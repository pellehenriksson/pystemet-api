from sqlmodel import create_engine, text, SQLModel
from sqlmodel.ext.asyncio.session import AsyncSession

from sqlalchemy import URL
from sqlalchemy.ext.asyncio import AsyncEngine
from sqlalchemy.orm import sessionmaker

#from ..config import Config

engine = AsyncEngine(create_engine(url="postgresql+asyncpg://postgres:pelle666@localhost/pystemet", echo=True))

async def init_db() -> None:
    async with engine.begin() as connection:
        from .schemas import Producer
        from .schemas import Supplier
        
        await connection.run_sync(SQLModel.metadata.create_all)

        #sql = text("SELECT 'Hello SQL'")
        #result = await connection.execute(sql)
        #print(result.all())

async def get_session() -> AsyncSession:

    Session = sessionmaker(bind = engine, class_ = AsyncSession, expire_on_commit = False)
    
    async with Session() as session:
        yield session