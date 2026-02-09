from sqlalchemy.orm import Session
from . import models

def check_project_completed(project: models.Project):
    project.completed = all(place.visited for place in project.places)


def can_delete_project(project: models.Project) -> bool:
    return not any(place.visited for place in project.places)
