from fastapi import FastAPI, HTTPException, Header, Query
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="Simple Plant API",
    description="A beginner-friendly REST API containing information about plants.",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)

# PLANT DATA
plants = [

    {
        "id": 1,
        "common_name": "Rose",
        "scientific_name": "Rosa",
        "family": "Rosaceae",
        "genus": "Rosa",
        "plant_type": "Flowering Plant",
        "origin": "Asia, Europe, North America, and Northwest Africa",
        "habitat": "Gardens, temperate forests, grasslands",
        "lifespan": "Perennial",
        "height_m": 2.0,
        "spread_m": 1.5,
        "sunlight": "Full Sun",
        "water_requirement": "Moderate",
        "soil_type": "Well-drained loamy soil",
        "flower_color": "Red, pink, white, yellow, orange",
        "flowering_season": "Spring to Autumn",
        "uses": "Ornamental, perfume, cosmetics",
        "toxicity": "Non-toxic",
        "description": "A widely cultivated flowering plant known for its fragrant and colorful flowers and thorny stems."
    },
    {
        "id": 2,
        "common_name": "Sunflower",
        "scientific_name": "Helianthus annuus",
        "family": "Asteraceae",
        "genus": "Helianthus",
        "plant_type": "Annual Herb",
        "origin": "North America",
        "habitat": "Grasslands, fields, agricultural areas",
        "lifespan": "Annual",
        "height_m": 3.0,
        "spread_m": 0.6,
        "sunlight": "Full Sun",
        "water_requirement": "Moderate",
        "soil_type": "Well-drained fertile soil",
        "flower_color": "Yellow",
        "flowering_season": "Summer",
        "uses": "Oil production, food, ornamental",
        "toxicity": "Non-toxic",
        "description": "A tall annual plant recognized by its large yellow flower head and edible seeds."
    },

]

# HOME
@app.get("/")
def home():

    return {
        "message": "Welcome to the Simple Plant API!",
        "endpoints": [
            "/plants",
            "/plants/{id}",
            "/plants/search"
        ]
    }


# GET ALL PLANTS
@app.get("/plants")
def get_plants():

    return {
        "count": len(plants),
        "plants": plants
    }

# SEARCH PLANTS
@app.get("/plants/search")
def search_plants( q: str = Query(..., min_length=1)):
    q = q.lower()
    results = []
    for plant in plants:
        searchable_text = (
            f"{plant['common_name']} "
            f"{plant['scientific_name']} "
            f"{plant['family']} "
            f"{plant['genus']}"
            f"{plant['plant_type']}"
            f"{plant['origin']}"
            f"{plant['habitat']}"
            f"{plant['lifespan']}"
            f"{plant['height_m']}"
            f"{plant['spread_m']}"
            f"{plant['sunlight']}"
            f"{plant['water_requirement']}"
            f"{plant['soil_type']}"
            f"{plant['flower_color']}"
            f"{plant['flowering_season']}"
            f"{plant['uses']}"
            f"{plant['toxicity']}"
            f"{plant['description']}"
        ).lower()

        if q in searchable_text:
            results.append(plant)

    return {
        "query": q,
        "count": len(results),
        "results": results
    }

# GET ONE PLANT
@app.get("/plants/{plant_id}")
def get_plant(plant_id: int):

    for plant in plants:

        if plant["id"] == plant_id:
            return plant

    raise HTTPException(
        status_code=404,
        detail="plant not found."
    )
