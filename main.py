import databases
import sqlalchemy
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

import settings
import tables
from routers import index, articles

app = FastAPI()
app.include_router(index.router)
app.include_router(articles.router)
app.mount(settings.STATIC_URL, StaticFiles(directory=settings.STATIC_DIRECTORY), name="static")

database = databases.Database(settings.DATABASE_URL)
engine = sqlalchemy.create_engine(settings.DATABASE_URL, connect_args={"check_same_thread": False})
tables.metadata.create_all(engine)


@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()
