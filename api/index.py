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
    {
        "id": 2,
        "country": "United States",
        "manufacturer": "General Dynamics Land Systems",
        "model": "M1A2 Abrams",
        "type": "Main Battle Tank",
        "year_introduced": 1992,
        "weight_tons": 63.5,
        "crew": 4,
        "engine": "Honeywell AGT1500",
        "horsepower": 1500,
        "max_speed_kmh": 67,
        "range_km": 425,
        "armor_type": "Composite armor",
        "description": "An American main battle tank known for heavy protection, mobility, and advanced electronic systems."
    },
    {
        "id": 3,
        "country": "United Kingdom",
        "manufacturer": "Vickers Defence Systems",
        "model": "Challenger 2",
        "type": "Main Battle Tank",
        "year_introduced": 1998,
        "weight_tons": 62.5,
        "crew": 4,
        "engine": "Perkins CV12",
        "horsepower": 1200,
        "max_speed_kmh": 59,
        "range_km": 550,
        "armor_type": "Chobham composite armor",
        "description": "A British main battle tank designed with an emphasis on protection and battlefield survivability."
    },
    {
        "id": 4,
        "country": "Soviet Union",
        "manufacturer": "Uralvagonzavod",
        "model": "T-72",
        "type": "Main Battle Tank",
        "year_introduced": 1969,
        "weight_tons": 41.0,
        "crew": 3,
        "engine": "V-46 diesel",
        "horsepower": 780,
        "max_speed_kmh": 60,
        "range_km": 500,
        "armor_type": "Steel and composite armor",
        "description": "A widely produced Soviet main battle tank recognized for its compact design and relatively low weight."
    },
    {
        "id": 5,
        "country": "Soviet Union",
        "manufacturer": "Malyshev Factory",
        "model": "T-64",
        "type": "Main Battle Tank",
        "year_introduced": 1966,
        "weight_tons": 38.0,
        "crew": 3,
        "engine": "5TDF diesel",
        "horsepower": 700,
        "max_speed_kmh": 60,
        "range_km": 500,
        "armor_type": "Composite armor",
        "description": "An influential Soviet main battle tank that introduced several advanced design features for its era."
    },
    {
        "id": 6,
        "country": "Russia",
        "manufacturer": "Uralvagonzavod",
        "model": "T-90",
        "type": "Main Battle Tank",
        "year_introduced": 1992,
        "weight_tons": 46.5,
        "crew": 3,
        "engine": "V-92S2 diesel",
        "horsepower": 1000,
        "max_speed_kmh": 60,
        "range_km": 550,
        "armor_type": "Composite and reactive armor",
        "description": "A Russian main battle tank developed from the T-72 family with improved protection and electronic systems."
    },
    {
        "id": 7,
        "country": "France",
        "manufacturer": "GIAT Industries",
        "model": "Leclerc",
        "type": "Main Battle Tank",
        "year_introduced": 1992,
        "weight_tons": 57.0,
        "crew": 3,
        "engine": "SACM V8X-1500",
        "horsepower": 1500,
        "max_speed_kmh": 72,
        "range_km": 550,
        "armor_type": "Modular composite armor",
        "description": "A French main battle tank featuring advanced automation, mobility, and digital battlefield systems."
    },
    {
        "id": 8,
        "country": "Israel",
        "manufacturer": "Israel Military Industries",
        "model": "Merkava Mk 4",
        "type": "Main Battle Tank",
        "year_introduced": 2004,
        "weight_tons": 65.0,
        "crew": 4,
        "engine": "General Dynamics GD883",
        "horsepower": 1500,
        "max_speed_kmh": 64,
        "range_km": 500,
        "armor_type": "Modular composite armor",
        "description": "An Israeli main battle tank designed with a strong emphasis on crew protection and battlefield adaptability."
    },
    {
        "id": 9,
        "country": "Japan",
        "manufacturer": "Mitsubishi Heavy Industries",
        "model": "Type 90",
        "type": "Main Battle Tank",
        "year_introduced": 1990,
        "weight_tons": 50.2,
        "crew": 3,
        "engine": "Mitsubishi 10ZG diesel",
        "horsepower": 1500,
        "max_speed_kmh": 70,
        "range_km": 350,
        "armor_type": "Composite armor",
        "description": "A Japanese main battle tank designed for high mobility and modern armored warfare requirements."
    },
    {
        "id": 10,
        "country": "South Korea",
        "manufacturer": "Hyundai Rotem",
        "model": "K2 Black Panther",
        "type": "Main Battle Tank",
        "year_introduced": 2014,
        "weight_tons": 55.0,
        "crew": 3,
        "engine": "Doosan DV27K diesel",
        "horsepower": 1500,
        "max_speed_kmh": 70,
        "range_km": 450,
        "armor_type": "Composite and reactive armor",
        "description": "A modern South Korean main battle tank featuring advanced mobility, electronics, and protection systems."
    },
    {
        "id": 11,
        "country": "United States",
        "manufacturer": "Chrysler Defense",
        "model": "M60 Patton",
        "type": "Main Battle Tank",
        "year_introduced": 1960,
        "weight_tons": 52.6,
        "crew": 4,
        "engine": "Continental AVDS-1790",
        "horsepower": 750,
        "max_speed_kmh": 48,
        "range_km": 480,
        "armor_type": "Rolled homogeneous steel",
        "description": "An American main battle tank widely used by the United States and numerous allied countries during the Cold War."
    },
    {
        "id": 12,
        "country": "Germany",
        "manufacturer": "Krauss-Maffei",
        "model": "Leopard 1",
        "type": "Main Battle Tank",
        "year_introduced": 1965,
        "weight_tons": 42.2,
        "crew": 4,
        "engine": "MTU MB 838 CaM 500",
        "horsepower": 830,
        "max_speed_kmh": 65,
        "range_km": 600,
        "armor_type": "Rolled homogeneous steel",
        "description": "A German Cold War main battle tank emphasizing mobility and conventional armored vehicle design."
    },
    {
        "id": 13,
        "country": "United States",
        "manufacturer": "Ford Motor Company",
        "model": "M4 Sherman",
        "type": "Medium Tank",
        "year_introduced": 1942,
        "weight_tons": 30.3,
        "crew": 5,
        "engine": "Continental R975 radial",
        "horsepower": 400,
        "max_speed_kmh": 48,
        "range_km": 193,
        "armor_type": "Rolled homogeneous steel",
        "description": "An American medium tank that became one of the most widely produced armored vehicles of World War II."
    },
    {
        "id": 14,
        "country": "Soviet Union",
        "manufacturer": "Kirov Plant",
        "model": "T-34",
        "type": "Medium Tank",
        "year_introduced": 1940,
        "weight_tons": 26.5,
        "crew": 4,
        "engine": "V-2 diesel",
        "horsepower": 500,
        "max_speed_kmh": 53,
        "range_km": 300,
        "armor_type": "Sloped rolled steel",
        "description": "A famous Soviet medium tank of World War II known for its combination of mobility, armor, and mass production."
    },
    {
        "id": 15,
        "country": "Germany",
        "manufacturer": "MAN",
        "model": "Panther",
        "type": "Medium Tank",
        "year_introduced": 1943,
        "weight_tons": 44.8,
        "crew": 5,
        "engine": "Maybach HL230",
        "horsepower": 700,
        "max_speed_kmh": 55,
        "range_km": 250,
        "armor_type": "Sloped rolled steel",
        "description": "A German medium tank from World War II recognized for its sloped armor and influential armored vehicle design."
    },
    {
        "id": 16,
        "country": "Italy",
        "manufacturer": "Oto Melara",
        "model": "Ariete",
        "type": "Main Battle Tank",
        "year_introduced": 1995,
        "weight_tons": 54.0,
        "crew": 4,
        "engine": "Iveco V12 diesel",
        "horsepower": 1300,
        "max_speed_kmh": 65,
        "range_km": 550,
        "armor_type": "Composite armor",
        "description": "Italy's primary main battle tank, designed for a balance of mobility, protection, and battlefield performance."
    },
    {
        "id": 17,
        "country": "China",
        "manufacturer": "Norinco",
        "model": "Type 99",
        "type": "Main Battle Tank",
        "year_introduced": 2001,
        "weight_tons": 55.0,
        "crew": 3,
        "engine": "Diesel engine",
        "horsepower": 1500,
        "max_speed_kmh": 80,
        "range_km": 600,
        "armor_type": "Composite and reactive armor",
        "description": "A Chinese main battle tank incorporating modern protection, mobility, and electronic systems."
    },
    {
        "id": 18,
        "country": "Sweden",
        "manufacturer": "Hägglunds",
        "model": "Stridsvagn 103",
        "type": "Main Battle Tank",
        "year_introduced": 1967,
        "weight_tons": 42.5,
        "crew": 3,
        "engine": "Rolls-Royce K60 diesel",
        "horsepower": 240,
        "max_speed_kmh": 60,
        "range_km": 390,
        "armor_type": "Sloped steel armor",
        "description": "An unusual Swedish tank recognized for its turretless design and low-profile configuration."
    },
    {
        "id": 19,
        "country": "France",
        "manufacturer": "AMX",
        "model": "AMX-30",
        "type": "Main Battle Tank",
        "year_introduced": 1966,
        "weight_tons": 36.0,
        "crew": 4,
        "engine": "Hispano-Suiza HS-110",
        "horsepower": 720,
        "max_speed_kmh": 65,
        "range_km": 500,
        "armor_type": "Rolled homogeneous steel",
        "description": "A French Cold War main battle tank designed around mobility and a relatively lightweight configuration."
    },
    {
        "id": 20,
        "country": "United States",
        "manufacturer": "Chrysler Defense",
        "model": "M48 Patton",
        "type": "Main Battle Tank",
        "year_introduced": 1952,
        "weight_tons": 49.6,
        "crew": 4,
        "engine": "Continental AVDS-1790",
        "horsepower": 750,
        "max_speed_kmh": 48,
        "range_km": 460,
        "armor_type": "Cast steel armor",
        "description": "A Cold War-era American main battle tank that served with many countries around the world."
    }

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
