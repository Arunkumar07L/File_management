from fastapi import APIRouter
from app.db.schemas import FileInfo,FileRenameInfo,FileDeleteInfo,FileMoveInfo
from app.services.file_service import create_file,rename_file,delete_file,move_file

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