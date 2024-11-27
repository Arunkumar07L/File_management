from app.db.session import db
from app.db.models import Folder
import os
import shutil
from app.services import get_path

def create_folder(data):
    new_folder = Folder(name=data.name, type=data.type, parent_id=data.parent_id)
    db.add(new_folder)
    db.commit()
    path = get_path(data.name,data.parent_id)
    os.mkdir(path)
    return {"message" : "Folder Created Successfully","folder_path" : path}

def move_folder(data):
    folder = db.query(Folder).filter(Folder.id==data.folder_id).first()
    move = db.query(Folder).filter(Folder.id==data.move_to).first()
    folder_path = get_path(folder.name,folder.parent_id)
    moved_path = os.path.join(get_path(move.name,move.parent_id),folder_path.split("\\")[-2])
    os.mkdir(moved_path)
    os.rmdir(folder_path)
    folder.parent_id = move.id
    db.commit()
    return {"message" : "Folder Moved Successfully","previous_path" : folder_path, "current_path" : moved_path}

def delete_folder(data):
    folder = db.query(Folder).filter(Folder.id==data.folder_id).first()
    folder_path = get_path(folder.name,folder.parent_id)
    shutil.rmtree(folder_path)
    db.delete(folder)
    db.commit()
    # for root, dirs, files in os.walk(folder_path, topdown=False):
    #     for dir in dirs:
    #             dir_path = os.path.join(root, dir)
    #             os.rmdir(dir_path)
    # os.rmdir(folder_path)
    return {"message" : "Folder Deleted Successfully"}

def rename_folder(data):
    folder = db.query(Folder).filter(Folder.id==data.folder_id).first()
    folder_path = get_path(folder.name,folder.parent_id)
    new_path = os.path.join("\\".join(folder_path.split("\\")[:-2]),data.new_name)
    os.rename(folder_path,new_path)
    folder.name = data.new_name
    db.commit()
    return {"message" : "Folder Renamed Successfully","previous_name" : folder_path, "new_name" :new_path}

def folder_contents(data):
    folder = db.query(Folder).filter(Folder.id==data.folder_id).first()
    folder_path = get_path(folder.name,folder.parent_id)
    contents = {}
    for root, dirs, files in os.walk(folder_path):
        contents[root] = {
            "dirs" : dirs,
            "files" : files
        }
    
    return {"Root":contents}