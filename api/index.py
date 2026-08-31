from fastapi import FastAPI, HTTPException, Header, Query
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="Simple Tank API",
    description="A beginner-friendly REST API containing information about tanks.",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)

# CAR DATA
tanks = [

    {
        "id": 1,
        "country": "Germany",
        "manufacturer": "Krauss-Maffei Wegmann",
        "model": "Leopard 2A7",
        "type": "Main Battle Tank",
        "year_introduced": 2014,
        "weight_tons": 66.5,
        "crew": 4,
        "engine": "MTU MB 873 Ka-501",
        "horsepower": 1500,
        "max_speed_kmh": 68,
        "range_km": 340,
        "armor_type": "Composite armor",
        "description": "A modern German main battle tank emphasizing protection, mobility, and advanced battlefield systems."
    },

]

# HOME
@app.get("/")
def home():

    return {
        "message": "Welcome to the Simple Tank API!",
        "endpoints": [
            "/tanks",
            "/tanks/{id}",
            "/tanks/search"
        ]
    }


# GET ALL TANKS
@app.get("/tanks")
def get_cars():

    return {
        "count": len(tanks),
        "tanks": tanks
    }

# SEARCH TANKS
@app.get("/tanks/search")
def search_tanks( q: str = Query(..., min_length=1)):
    q = q.lower()
    results = []
    for tank in tanks:
        searchable_text = (
            f"{tank['country']} "
            f"{tank['manufacturer']} "
            f"{tank['model']} "
            f"{tank['type']}"
            f"{tank['year_introduced']}"
            f"{tank['weight_tons']}"
            f"{tank['crew']}"
            f"{tank['engine']}"
            f"{tank['horsepower']}"
            f"{tank['max_speed_kmh']}"
            f"{tank['range_km']}"
            f"{tank['armor_type']}"
            f"{tank['description']}"
        ).lower()

        if q in searchable_text:
            results.append(tank)

    return {
        "query": q,
        "count": len(results),
        "results": results
    }

# GET ONE TANK
@app.get("/tanks/{tank_id}")
def get_tank(tank_id: int):

    for tank in tanks:

        if tank["id"] == tank_id:
            return tank

    raise HTTPException(
        status_code=404,
        detail="Tank not found."
    )
