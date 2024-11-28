from fastapi import FastAPI
from app.api import folders,files
import uvicorn

app = FastAPI()

app.include_router(folders.router, prefix="/folders", tags=["Folders"])
app.include_router(files.router, prefix="/files", tags=["Files"])



if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8000,
        reload=True
    )
