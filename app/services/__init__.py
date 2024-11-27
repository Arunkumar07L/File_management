import os
from app.db.models import Folder
from app.db.session import db

base_path = os.path.join(os.path.normpath(os.path.join(os.getcwd(), "..")), "Directory")
os.mkdir(base_path)

def get_path(name, parent_id, sub_path=""):
    sub_path = os.path.join(name, sub_path) if name else sub_path

    if parent_id:
        parent_folder = db.query(Folder).filter(Folder.id == parent_id).first()
        if parent_folder:
            return get_path(parent_folder.name, parent_folder.parent_id, sub_path)
        else:
            raise ValueError(f"No folder found with id: {parent_id}")
    else:
        return os.path.join(base_path, sub_path)[:-1]