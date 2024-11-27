from pydantic import BaseModel


class FolderInfo(BaseModel):
    name: str
    type : str
    parent_id : int | None = None
        
class FolderMoveInfo(BaseModel):
    folder_id : int
    move_to : int
    
class FolderDeleteInfo(BaseModel):
    folder_id : int

class FolderRenameInfo(BaseModel):
    folder_id : int
    new_name : str
    
class FolderListInfo(BaseModel):
    folder_id : int
    
class FileInfo(BaseModel):
    name: str
    type : str
    parent_id : int | None = None
    
class FileMoveInfo(BaseModel):
    file_id : int
    move_to : int
    
class FileRenameInfo(BaseModel):
    file_id : int
    new_name : str
    
class FileDeleteInfo(BaseModel):
    file_id : int