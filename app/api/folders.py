from fastapi import APIRouter
from app.services.folder_service import create_folder,move_folder,delete_folder,rename_folder
from app.db.schemas import FolderInfo,FolderMoveInfo,FolderDeleteInfo,FolderRenameInfo


router = APIRouter()

@router.post("/create")
def folder_creation(data:FolderInfo):
    return create_folder(data)

@router.post("/move")
def folder_moving(data:FolderMoveInfo):
    return move_folder(data)

@router.post("/delete")
def folder_deletion(data:FolderDeleteInfo):
    return delete_folder(data)

@router.post("/rename")
def folder_renaming(data:FolderRenameInfo):
    return rename_folder(data)