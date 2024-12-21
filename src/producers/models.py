from pydantic import BaseModel

class ProducerViewModel(BaseModel):
    id: int
    name: str