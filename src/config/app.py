from fastapi import FastAPI

from config import env
from routes import root_route

app = FastAPI(
    title="Striter Aggregation Service",
    version="0.0.0",
    docs_url="/api/v1/docs/",
    redoc_url="/api/v1/redocs/",
    debug=env.DEBUG,
)

app.include_router(root_route.router)
