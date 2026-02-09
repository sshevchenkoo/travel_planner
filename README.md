# travel_planner
Travel Projects Management API

Backend CRUD application for managing travel projects and places to visit.
Built as a test assignment to demonstrate RESTful API design, database interaction, and third-party API integration.

▶️ Run locally (without Docker)
python -m venv venv
source venv/bin/activate

pip install -r requirements.txt

uvicorn app.main:app --reload


API will be available at:
http://127.0.0.1:8000

Swagger UI:
http://127.0.0.1:8000/docs

Example API Requests
Create a project with places

external_id must exist in the Art Institute of Chicago API

curl -X POST \
  http://127.0.0.1:8000/projects/ \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Berlin Art Tour",
    "description": "Exploring famous artworks",
    "start_date": "2026-03-15",
    "places": [
      {
        "external_id": 129884,
        "notes": "Must see"
      }
    ]
  }'

Get all projects
curl -X GET http://127.0.0.1:8000/projects/

Update a project
curl -X PATCH \
  http://127.0.0.1:8000/projects/1 \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Updated Project Name"
  }'

Mark a place as visited
curl -X PATCH \
  http://127.0.0.1:8000/projects/1/places/1 \
  -H "Content-Type: application/json" \
  -d '{
    "visited": true
  }'

Delete a project
Project cannot be deleted if any place is marked as visited
curl -X DELETE http://127.0.0.1:8000/projects/1