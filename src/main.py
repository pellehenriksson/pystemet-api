from fastapi import Depends, FastAPI
from starlette.responses import RedirectResponse
from .producers import routes
from .db.main import init_db
from contextlib import asynccontextmanager

@asynccontextmanager
async def lifespan(app: FastAPI):
    print("Server is starting...")
    await init_db()
    yield
    print("Server has been stopped")

version = "v1"

app = FastAPI(
    title="Pystemet API", 
    description="REST API for systembolaget products", 
    version=version,
    lifespan=lifespan)

app.include_router(routes.router)

@app.get("/")
def root():
    return RedirectResponse(url="/docs")