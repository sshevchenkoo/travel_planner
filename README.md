# travel_planner
Travel Projects Management API

Backend CRUD application for managing travel projects and places to visit.
Built as a test assignment to demonstrate RESTful API design, database interaction, and third-party API integration.

▶️ Run locally (without Docker)
# Create virtual environment
python -m venv venv

# Activate virtual environment
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run FastAPI server
uvicorn app.main:app --reload


API will be available at:

http://127.0.0.1:8000


Swagger UI:

http://127.0.0.1:8000/docs

🧪 Example API Requests
1️⃣ Create a project with places

⚠️ external_id must exist in the Art Institute of Chicago API

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

2️⃣ Get all projects
curl -X GET http://127.0.0.1:8000/projects/

3️⃣ Update a project
curl -X PATCH \
  http://127.0.0.1:8000/projects/1 \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Updated Project Name"
  }'

4️⃣ Mark a place as visited
curl -X PATCH \
  http://127.0.0.1:8000/projects/1/places/1 \
  -H "Content-Type: application/json" \
  -d '{
    "visited": true
  }'

5️⃣ Delete a project

❌ Project cannot be deleted if any place is marked as visited

curl -X DELETE http://127.0.0.1:8000/projects/1