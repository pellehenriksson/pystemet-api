from sqlmodel import SQLModel, Field, Column
import sqlalchemy.dialects.postgresql as pg
from datetime import datetime

class Producer(SQLModel, table=True):
    __tablename__ = "producers"

    id: int | None = Field(default=None, primary_key=True)
    name: str = Field(index=True, nullable=False), 
    created_at: datetime = Field(Column(pg.TIMESTAMP, default=datetime.now))

    def __repr__(self):
        return f"<producer {self.name} >"