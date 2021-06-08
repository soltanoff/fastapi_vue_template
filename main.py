from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

import settings
from routers import index

app = FastAPI()
app.include_router(index.router)
app.mount(settings.STATIC_URL, StaticFiles(directory=settings.STATIC_DIRECTORY), name="static")
