from fastapi import FastAPI
from routes import root_route

from config import env

app = FastAPI(
    title="Stritter API Gateway",
    version="0.0.0",
    docs_url="/api/v1/docs/",
    redoc_url="/api/v1/redocs/",
    debug=env.DEBUG,
)

app.include_router(root_route.router)
