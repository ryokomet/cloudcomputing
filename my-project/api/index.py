from fastapi import FastAPI, HTTPException, Header, Query
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="Simple Car API",
    description="A beginner-friendly REST API containing information about cars.",
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
cars = [

    {
        "id": 1,
        "make": "Toyota",
        "model": "Corolla",
        "year": 1998,
        "engine": "1.6L 4-cylinder",
        "horsepower": 105,
        "description": "A practical and reliable compact sedan."
    },

    {
        "id": 2,
        "make": "Honda",
        "model": "Civic Si",
        "year": 1999,
        "engine": "1.6L 4-cylinder",
        "horsepower": 160,
        "description": "A sporty compact car popular with enthusiasts."
    },

    {
        "id": 3,
        "make": "Mitsubishi",
        "model": "Eclipse GSX",
        "year": 1999,
        "engine": "2.0L Turbo 4-cylinder",
        "horsepower": 210,
        "description": "A turbocharged AWD coupe built for performance."
    },

    {
        "id": 4,
        "make": "Subaru",
        "model": "Impreza WRX",
        "year": 2002,
        "engine": "2.0L Turbo 4-cylinder",
        "horsepower": 227,
        "description": "A turbocharged AWD performance sedan."
    },

    {
        "id": 5,
        "make": "Mazda",
        "model": "MX-5 Miata",
        "year": 2001,
        "engine": "1.8L 4-cylinder",
        "horsepower": 142,
        "description": "A lightweight two-seat roadster famous for its handling."
    }

]

# HOME
@app.get("/")
def home():

    return {
        "message": "Welcome to the Simple Car API!",
        "endpoints": [
            "/cars",
            "/cars/{id}",
            "/cars/search"
        ]
    }


# GET ALL CARS
@app.get("/cars")
def get_cars():

    return {
        "count": len(cars),
        "cars": cars
    }


# GET ONE CAR
@app.get("/cars/{car_id}")
def get_car(car_id: int):

    for car in cars:

        if car["id"] == car_id:
            return car

    raise HTTPException(
        status_code=404,
        detail="Car not found."
    )

# SEARCH CARS
@app.get("/cars/search")
def search_cars( q: str = Query(..., min_length=1)):
    q = q.lower()
    results = []
    for car in cars:
        searchable_text = (
            f"{car['make']} "
            f"{car['model']} "
            f"{car['year']} "
            f"{car['engine']}"
        ).lower()

        if q in searchable_text:
            results.append(car)

    return {
        "query": q,
        "count": len(results),
        "results": results
    }
