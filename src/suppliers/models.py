from pydantic import BaseModel

class SupplierViewModel(BaseModel):
    id: int
    name: str