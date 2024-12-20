from pydantic import BaseModel

class ItemTypeViewModel(BaseModel):
    id: int
    name: str