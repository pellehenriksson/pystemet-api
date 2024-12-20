from sqlmodel import SQLModel, Field, Column
import sqlalchemy.dialects.postgresql as pg
from datetime import datetime
from decimal import Decimal

class Producer(SQLModel, table=True):
    __tablename__ = "producers"

    id: int | None = Field(default=None, primary_key=True)
    name: str = Field(index=True, nullable=False), 
    created_at: datetime = Field(sa_column=Column(pg.TIMESTAMP, default=datetime.now))

    def __repr__(self):
        return f"<producer {self.name} >"
    
class Supplier(SQLModel, table=True):
    __tablename__ = "suppliers"

    id: int | None = Field(default=None, primary_key=True)
    name: str = Field(index=True, nullable=False), 
    created_at: datetime = Field(sa_column=Column(pg.TIMESTAMP, default=datetime.now))

    def __repr__(self):
        return f"<supplier {self.name} >"
    
class Item(SQLModel, table=True):
    __tablename__ = "items"

    id: int | None = Field(default=None, primary_key=True)
    number: str = Field(index=True, nullable=False), 
    name: str = Field(index=True, nullable=False), 
    price: Decimal = Field(default=None, max_digits=10, decimal_places=2)
    comparison_price: Decimal = Field(default=None, max_digits=10, decimal_places=2)
    volume: Decimal = Field(default=None, max_digits=10, decimal_places=2)
    alcohol_content: Decimal = Field(default=None, max_digits=10, decimal_places=2)
    packaging: str | None
    sealing: str | None
    origin: str | None
    origin_country: str | None
    is_organic: bool = Field(nullable=False)
    is_ethical: bool = Field(nullable=False)
    producer_id: int = Field(default=None, foreign_key="producers.id")
    supplier_id: int = Field(default=None, foreign_key="suppliers.id")
    item_type_id: int = Field(default=None, foreign_key="item_types.id")
    item_style_id: int | None  = Field(default=None, foreign_key="item_styles.id")
    created_at: datetime = Field(sa_column=Column(pg.TIMESTAMP, default=datetime.now))

    def __repr__(self):
        return f"<item {self.name} >"

class ItemStyle(SQLModel, table=True):
    __tablename__ = "item_styles"

    id: int | None = Field(default=None, primary_key=True)
    name: str = Field(index=True, nullable=False), 
    created_at: datetime = Field(sa_column=Column(pg.TIMESTAMP, default=datetime.now))

    def __repr__(self):
        return f"<item_style {self.name} >"
    
class ItemType(SQLModel, table=True):
    __tablename__ = "item_types"

    id: int | None = Field(default=None, primary_key=True)
    name: str = Field(index=True, nullable=False), 
    created_at: datetime = Field(sa_column=Column(pg.TIMESTAMP, default=datetime.now))

    def __repr__(self):
        return f"<item_type {self.name} >"