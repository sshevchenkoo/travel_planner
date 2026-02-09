from typing import Optional, List
from pydantic import BaseModel
from datetime import date

class PlaceCreate(BaseModel):
    external_id: int
    notes: Optional[str] = None 

class PlaceUpdate(BaseModel):
    notes: Optional[str] = None 
    visited: Optional[bool] = None 

class PlaceResponse(BaseModel):
    id: int
    external_id: int
    title: Optional[str] = None
    notes: Optional[str] = None
    visited: bool

    class Config:
        orm_mode = True


class ProjectCreate(BaseModel):
    name: str
    description: Optional[str] = None
    start_date: Optional[date] = None
    places: Optional[List[PlaceCreate]] = []

class ProjectUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    start_date: Optional[date] = None

class ProjectResponse(BaseModel):
    id: int
    name: str
    description: Optional[str] = None
    start_date: Optional[date] = None
    completed: bool
    places: List[PlaceResponse] = []

    class Config:
        orm_mode = True
