from fastapi import FastAPI

from routers.crud import router as crud_router
from routers.stats import router as stats_router

app = FastAPI()

app.include_router(crud_router)
app.include_router(stats_router)
