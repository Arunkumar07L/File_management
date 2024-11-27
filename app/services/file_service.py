from app.db.session import db
from app.db.models import File,Folder
from app.services import get_path
import os


def create_file(data):
    folder = db.query(Folder).filter(Folder.id==data.parent_id).first()
    folder_path = get_path(folder.name,folder.parent_id)
    file_path = os.path.join(folder_path, data.name)
    f = File(name=data.name,type=data.type,folder_id=data.parent_id)
    db.add(f)
    db.commit()
    with open(file_path,'w') as file:
        pass
    
    return {"message" : "File Created Successfully", "file_path" : file_path}

def move_file(data):
    file = db.query(File).filter(File.id==data.file_id).first()
    file_path = get_path(file.name,file.folder_id)
    move = db.query(Folder).filter(Folder.id==data.move_to).first()
    moved_path = os.path.join(get_path(move.name,move.parent_id),file_path.split("\\")[-1])

    with open(moved_path,"w") as f:
        pass
    os.remove(file_path)
    file.folder_id = move.id
    db.commit()
    
    return {"message" : "File Moved Successfully","previous_path" : file_path, "current_path" : moved_path}


def rename_file(data):
    file = db.query(File).filter(File.id==data.file_id).first()
    file_path = get_path(file.name,file.folder_id)
    new_path = os.path.join("\\".join(file_path.split("\\")[:-2]),data.new_name)
    os.rename(file_path,new_path)
    file.name = data.new_name
    db.commit()
    return {"message" : "File Renamed Successfully","previous_name" : file_path, "new_name" :new_path}

def delete_file(data):
    file = db.query(File).filter(File.id==data.file_id).first()
    file_path = get_path(file.name,file.folder_id)
    db.delete(file)
    db.commit()
    os.remove(file_path)
    
    return {"message" : "File Deleted Successfully"}