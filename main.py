from app.db.session import Base,engine
from fastapi import FastAPI
from app.api import folders,files

app = FastAPI()
# Base.metadata.create_all(bind=engine)

app.include_router(folders.router, prefix="/folders", tags=["Folders"])
app.include_router(files.router, prefix="/files", tags=["Files"])
