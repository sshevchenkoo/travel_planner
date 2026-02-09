import requests

BASE_URL = "https://api.artic.edu/api/v1/artworks"

def fetch_artwork(external_id: int):
    response = requests.get(f"{BASE_URL}/{external_id}")
    if response.status_code != 200:
        return None
    data = response.json().get("data")
    return data
