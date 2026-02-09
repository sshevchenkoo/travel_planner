from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..database import SessionLocal
from .. import models, schemas
from ..services.art_api import fetch_artwork
from ..crud import check_project_completed

router = APIRouter(prefix="/projects/{project_id}/places", tags=["Places"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/", response_model=schemas.PlaceResponse)
def add_place(project_id: int, place: schemas.PlaceCreate, db: Session = Depends(get_db)):
    project = db.query(models.Project).get(project_id)
    if not project:
        raise HTTPException(404, "Project not found")

    if len(project.places) >= 10:
        raise HTTPException(400, "Max 10 places allowed")

    if any(p.external_id == place.external_id for p in project.places):
        raise HTTPException(400, "Place already added")

    artwork = fetch_artwork(place.external_id)
    if not artwork:
        raise HTTPException(400, "Invalid external place ID")

    new_place = models.Place(
        external_id=place.external_id,
        title=artwork.get("title"),
        notes=place.notes
    )

    project.places.append(new_place)
    db.commit()
    db.refresh(new_place)
    return new_place

@router.patch("/{place_id}", response_model=schemas.PlaceResponse)
def update_place(
    project_id: int,
    place_id: int,
    place_update: schemas.PlaceUpdate,
    db: Session = Depends(get_db)
):
    project = db.query(models.Project).get(project_id)
    if not project:
        raise HTTPException(status_code=404, detail="Project not found")

    place = next((p for p in project.places if p.id == place_id), None)
    if not place:
        raise HTTPException(status_code=404, detail="Place not found in project")

    if place_update.notes is not None:
        place.notes = place_update.notes
    if place_update.visited is not None:
        place.visited = place_update.visited

    db.commit()
    db.refresh(place)
    return place
