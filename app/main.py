from fastapi import Depends, FastAPI
from .routers import producers

app = FastAPI(title="Pystemet API", summary="", dependencies=[])

app.include_router(producers.router)

@app.get("/")
async def read_root():
    return {"message": "hello world"}