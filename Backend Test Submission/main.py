from fastapi import FastAPI

from routers.crud import router as crud_router
from routers.stats import router as stats_router

import requests

app = FastAPI()

app.include_router(crud_router)
app.include_router(stats_router)

def log(stack: str, level: str, package: str, message: str):
	response = requests.post("http://localhost:4000/log", json={
		"stack": stack,
		"level": level,
		"package": package,
		"message": message
	})
	return response.json()
