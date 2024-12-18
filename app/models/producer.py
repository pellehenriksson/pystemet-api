from sqlmodel import SQLModel, Field

class Producer(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str = Field(index=True)