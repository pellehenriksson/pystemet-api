from fastapi import Depends, FastAPI
from starlette.responses import RedirectResponse
from .producers import routes as p_routes
from .suppliers import routes as s_routes
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

app.include_router(p_routes.router)
app.include_router(s_routes.router)

@app.get("/")
def root():
    return RedirectResponse(url="/docs")