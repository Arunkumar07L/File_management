from fastapi import FastAPI
from app.api import folders,files

app = FastAPI()

app.include_router(folders.router, prefix="/folders", tags=["Folders"])
app.include_router(files.router, prefix="/files", tags=["Files"])
