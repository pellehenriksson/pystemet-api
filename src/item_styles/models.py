from pydantic import BaseModel

class ItemStyleViewModel(BaseModel):
    id: int
    name: str