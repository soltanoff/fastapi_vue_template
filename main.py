from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from starlette.middleware.trustedhost import TrustedHostMiddleware

import settings
from routers import index, articles
from tables import database

app = FastAPI()
app.add_middleware(TrustedHostMiddleware, allowed_hosts=settings.ALLOWED_HOSTS)
app.include_router(index.router)
app.include_router(articles.router)
app.mount(settings.STATIC_URL, StaticFiles(directory=settings.STATIC_DIRECTORY), name="static")


@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()
