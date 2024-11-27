from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.db.session import Base

class Folder(Base):
    __tablename__ = "folders"
    
    id = Column(Integer,primary_key=True,autoincrement=True)
    name = Column(String,unique=True,nullable=False)
    type = Column(String,nullable=False)
    parent_id = Column(Integer, ForeignKey("folders.id"),nullable=True)
    
    subfolders = relationship("Folder", back_populates="parent", cascade="all, delete")
    parent = relationship("Folder", remote_side=[id], back_populates="subfolders")
    
    files = relationship("File", back_populates="folder", cascade="all, delete")
    
class File(Base):
    __tablename__ = "files"
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String,unique=True, nullable=False)
    type = Column(String,nullable=False)
    folder_id = Column(Integer, ForeignKey("folders.id"), nullable=False)
 
    folder = relationship("Folder", back_populates="files")
    