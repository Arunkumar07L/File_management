from fastapi import APIRouter,UploadFile,File,Request,Form
from app.db.schemas import FileInfo,FileRenameInfo,FileDeleteInfo,FileMoveInfo
from app.services.file_service import create_file,rename_file,delete_file,move_file,upload_file,upload_chunk
from fastapi.responses import HTMLResponse

router = APIRouter()

@router.post("/create")
def file_creation(data:FileInfo):
    return create_file(data)

@router.post("/move")
def file_moving(data:FileMoveInfo):
    return move_file(data)

@router.post("/rename")
def file_renaming(data:FileRenameInfo):
    return rename_file(data)

@router.post("/delete")
def file_deleting(data:FileDeleteInfo):
    return delete_file(data)

@router.get("/upload",response_class=HTMLResponse)
def file_upload(request : Request):
    return upload_file(request)

@router.post("/upload-chunk")
async def get_upload(file: UploadFile = File(...),index: int = Form(...), total_chunks: int = Form(...),file_type: str = Form(...)):
    return await upload_chunk(file,index,total_chunks,file_type)