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
        id: 1,
        common_name: "Rose",
        scientific_name: "Rosa",
        family: "Rosaceae",
        genus: "Rosa",
        plant_type: "Flowering Plant",
        origin: "Asia, Europe, North America, and Northwest Africa",
        habitat: "Gardens, temperate forests, grasslands",
        lifespan: "Perennial",
        height_m: 2.0,
        spread_m: 1.5,
        sunlight: "Full Sun",
        water_requirement: "Moderate",
        soil_type: "Well-drained loamy soil",
        flower_color: "Red, pink, white, yellow, orange",
        flowering_season: "Spring to Autumn",
        uses: "Ornamental, perfume, cosmetics",
        toxicity: "Non-toxic",
        description: "A widely cultivated flowering plant known for its fragrant and colorful flowers and thorny stems."
    },
    {
        id: 2,
        common_name: "Sunflower",
        scientific_name: "Helianthus annuus",
        family: "Asteraceae",
        genus: "Helianthus",
        plant_type: "Annual Herb",
        origin: "North America",
        habitat: "Grasslands, fields, agricultural areas",
        lifespan: "Annual",
        height_m: 3.0,
        spread_m: 0.6,
        sunlight: "Full Sun",
        water_requirement: "Moderate",
        soil_type: "Well-drained fertile soil",
        flower_color: "Yellow",
        flowering_season: "Summer",
        uses: "Oil production, food, ornamental",
        toxicity: "Non-toxic",
        description: "A tall annual plant recognized by its large yellow flower head and edible seeds."
    },
    {
        id: 3,
        common_name: "Lavender",
        scientific_name: "Lavandula angustifolia",
        family: "Lamiaceae",
        genus: "Lavandula",
        plant_type: "Herbaceous Perennial",
        origin: "Mediterranean region",
        habitat: "Dry hillsides, rocky slopes, gardens",
        lifespan: "Perennial",
        height_m: 0.8,
        spread_m: 0.8,
        sunlight: "Full Sun",
        water_requirement: "Low",
        soil_type: "Dry, well-drained alkaline soil",
        flower_color: "Purple",
        flowering_season: "Summer",
        uses: "Essential oils, perfume, ornamental",
        toxicity: "Generally non-toxic",
        description: "An aromatic Mediterranean herb valued for its purple flowers and distinctive fragrance."
    },
    {
        id: 4,
        common_name: "Aloe Vera",
        scientific_name: "Aloe vera",
        family: "Asphodelaceae",
        genus: "Aloe",
        plant_type: "Succulent",
        origin: "Arabian Peninsula",
        habitat: "Arid and semi-arid regions",
        lifespan: "Perennial",
        height_m: 0.8,
        spread_m: 0.6,
        sunlight: "Full Sun to Partial Shade",
        water_requirement: "Low",
        soil_type: "Sandy, well-drained soil",
        flower_color: "Yellow",
        flowering_season: "Winter to Spring",
        uses: "Cosmetics, skincare, ornamental",
        toxicity: "Toxic if ingested in large quantities",
        description: "A drought-tolerant succulent with thick fleshy leaves commonly grown for ornamental and cosmetic purposes."
    },
    {
        id: 5,
        common_name: "Mango",
        scientific_name: "Mangifera indica",
        family: "Anacardiaceae",
        genus: "Mangifera",
        plant_type: "Fruit Tree",
        origin: "South Asia",
        habitat: "Tropical forests and cultivated areas",
        lifespan: "Perennial",
        height_m: 30.0,
        spread_m: 12.0,
        sunlight: "Full Sun",
        water_requirement: "Moderate",
        soil_type: "Deep, well-drained loamy soil",
        flower_color: "White to Pink",
        flowering_season: "Winter to Spring",
        uses: "Fruit production, food, shade",
        toxicity: "Fruit is edible; sap may cause skin irritation",
        description: "A large tropical evergreen tree cultivated worldwide for its sweet and nutritious fruit."
    },
    {
        id: 6,
        common_name: "Basil",
        scientific_name: "Ocimum basilicum",
        family: "Lamiaceae",
        genus: "Ocimum",
        plant_type: "Herb",
        origin: "Tropical Asia and Africa",
        habitat: "Gardens, farms, warm temperate regions",
        lifespan: "Annual or Short-lived Perennial",
        height_m: 0.6,
        spread_m: 0.4,
        sunlight: "Full Sun",
        water_requirement: "Moderate",
        soil_type: "Rich, well-drained soil",
        flower_color: "White or Purple",
        flowering_season: "Summer",
        uses: "Culinary herb, essential oils",
        toxicity: "Generally non-toxic",
        description: "An aromatic herb widely used in cooking and particularly associated with Mediterranean and Southeast Asian cuisines."
    },
    {
        id: 7,
        common_name: "Snake Plant",
        scientific_name: "Dracaena trifasciata",
        family: "Asparagaceae",
        genus: "Dracaena",
        plant_type: "Succulent Herb",
        origin: "Tropical West Africa",
        habitat: "Dry tropical forests and rocky areas",
        lifespan: "Perennial",
        height_m: 1.2,
        spread_m: 0.5,
        sunlight: "Low Light to Full Sun",
        water_requirement: "Low",
        soil_type: "Sandy, well-drained soil",
        flower_color: "Greenish White",
        flowering_season: "Rarely Blooms",
        uses: "Ornamental, indoor plant",
        toxicity: "Toxic if ingested",
        description: "A hardy indoor plant recognized for its upright sword-shaped leaves and tolerance of low-light conditions."
    },
    {
        id: 8,
        common_name: "Peace Lily",
        scientific_name: "Spathiphyllum",
        family: "Araceae",
        genus: "Spathiphyllum",
        plant_type: "Herbaceous Perennial",
        origin: "Tropical Americas and Southeast Asia",
        habitat: "Tropical rainforests",
        lifespan: "Perennial",
        height_m: 0.8,
        spread_m: 0.6,
        sunlight: "Partial Shade",
        water_requirement: "Moderate to High",
        soil_type: "Moist, well-drained soil",
        flower_color: "White",
        flowering_season: "Spring to Summer",
        uses: "Indoor ornamental plant",
        toxicity: "Toxic if ingested",
        description: "A popular tropical houseplant known for its dark green leaves and distinctive white flower-like spathes."
    },
    {
        id: 9,
        common_name: "Bamboo",
        scientific_name: "Bambusa vulgaris",
        family: "Poaceae",
        genus: "Bambusa",
        plant_type: "Grass",
        origin: "Asia",
        habitat: "Tropical and subtropical regions",
        lifespan: "Perennial",
        height_m: 15.0,
        spread_m: 5.0,
        sunlight: "Full Sun to Partial Shade",
        water_requirement: "High",
        soil_type: "Moist, well-drained fertile soil",
        flower_color: "Rarely Flowers",
        flowering_season: "Irregular",
        uses: "Construction, furniture, crafts, ornamental",
        toxicity: "Generally non-toxic",
        description: "A fast-growing perennial grass with hollow stems that is widely used for construction, crafts, and landscaping."
    },
    {
        id: 10,
        common_name: "Orchid",
        scientific_name: "Phalaenopsis amabilis",
        family: "Orchidaceae",
        genus: "Phalaenopsis",
        plant_type: "Epiphytic Orchid",
        origin: "Southeast Asia and Australia",
        habitat: "Tropical forests",
        lifespan: "Perennial",
        height_m: 0.7,
        spread_m: 0.5,
        sunlight: "Bright Indirect Light",
        water_requirement: "Moderate",
        soil_type: "Bark-based or porous orchid medium",
        flower_color: "White",
        flowering_season: "Year-round",
        uses: "Ornamental, floral arrangements",
        toxicity: "Non-toxic",
        description: "A tropical orchid prized for its elegant white flowers and popularity as an indoor ornamental plant."
    },
    {
        id: 11,
        common_name: "Coconut Palm",
        scientific_name: "Cocos nucifera",
        family: "Arecaceae",
        genus: "Cocos",
        plant_type: "Palm Tree",
        origin: "Tropical Indo-Pacific",
        habitat: "Tropical coastal regions",
        lifespan: "Perennial",
        height_m: 30.0,
        spread_m: 7.0,
        sunlight: "Full Sun",
        water_requirement: "High",
        soil_type: "Sandy, well-drained soil",
        flower_color: "Cream to Yellow",
        flowering_season: "Year-round",
        uses: "Food, oil, fiber, construction",
        toxicity: "Non-toxic",
        description: "A tropical palm widely cultivated for its versatile fruit, edible meat, coconut water, oil, and fibrous husks."
    },
    {
        id: 12,
        common_name: "Venus Flytrap",
        scientific_name: "Dionaea muscipula",
        family: "Droseraceae",
        genus: "Dionaea",
        plant_type: "Carnivorous Plant",
        origin: "Southeastern United States",
        habitat: "Wetlands, bogs, savannas",
        lifespan: "Perennial",
        height_m: 0.2,
        spread_m: 0.2,
        sunlight: "Full Sun",
        water_requirement: "High",
        soil_type: "Acidic, nutrient-poor soil",
        flower_color: "White",
        flowering_season: "Spring",
        uses: "Ornamental, educational",
        toxicity: "Non-toxic",
        description: "A carnivorous plant that captures insects using specialized hinged leaves that rapidly close when triggered."
    },
    {
        id: 13,
        common_name: "Pitcher Plant",
        scientific_name: "Nepenthes alata",
        family: "Nepenthaceae",
        genus: "Nepenthes",
        plant_type: "Carnivorous Vine",
        origin: "Philippines",
        habitat: "Tropical forests and mountainous regions",
        lifespan: "Perennial",
        height_m: 1.5,
        spread_m: 1.0,
        sunlight: "Bright Indirect Light",
        water_requirement: "High",
        soil_type: "Acidic, nutrient-poor soil",
        flower_color: "Green to Red",
        flowering_season: "Seasonal",
        uses: "Ornamental, educational",
        toxicity: "Non-toxic",
        description: "A tropical carnivorous plant that develops pitcher-shaped traps filled with digestive fluid for capturing insects."
    },
    {
        id: 14,
        common_name: "Neem",
        scientific_name: "Azadirachta indica",
        family: "Meliaceae",
        genus: "Azadirachta",
        plant_type: "Evergreen Tree",
        origin: "Indian Subcontinent",
        habitat: "Tropical and subtropical regions",
        lifespan: "Perennial",
        height_m: 20.0,
        spread_m: 15.0,
        sunlight: "Full Sun",
        water_requirement: "Low to Moderate",
        soil_type: "Well-drained sandy or loamy soil",
        flower_color: "White",
        flowering_season: "Spring",
        uses: "Traditional products, insect repellent, shade",
        toxicity: "Seeds and oil can be toxic if improperly consumed",
        description: "A hardy evergreen tree valued for its traditional uses and natural insect-repellent properties."
    },
    {
        id: 15,
        common_name: "Acacia",
        scientific_name: "Acacia mangium",
        family: "Fabaceae",
        genus: "Acacia",
        plant_type: "Evergreen Tree",
        origin: "Australia and Papua New Guinea",
        habitat: "Tropical forests and plantations",
        lifespan: "Perennial",
        height_m: 30.0,
        spread_m: 10.0,
        sunlight: "Full Sun",
        water_requirement: "Moderate",
        soil_type: "Well-drained acidic to neutral soil",
        flower_color: "Cream to Yellow",
        flowering_season: "Seasonal",
        uses: "Timber, reforestation, paper production",
        toxicity: "Some species contain toxic compounds",
        description: "A fast-growing tropical tree commonly cultivated for timber, pulp production, and reforestation."
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
