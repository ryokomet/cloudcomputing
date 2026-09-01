const API_URL = "https://ryokomet-cloudcomputing.vercel.app";


// API REQUEST HELPER

async function fetchAPI(endpoint) {
    const response = await fetch(`${API_URL}${endpoint}`);

    if (!response.ok) {
        throw new Error(`API Error: ${response.status}`);
    }

    return await response.json();
}


// GET ALL PLANTS

async function loadPlants() {
    const plantList = document.getElementById("plantList");

    plantList.innerHTML = "<p>Loading plants...</p>";

    try {
        const data = await fetchAPI("/plants");

        displayPlants(data.plants);
    }

    catch (error) {
        console.error("Failed to load plants:", error);

        plantList.innerHTML =
            "<p>Unable to connect to the API.</p>";
    }
}


// DISPLAY PLANTS

function slugify(text) {
    return text.toLowerCase().trim().replace(/\s+/g, '-');
}

function displayPlants(plants) {
    const plantList = document.getElementById("plantList");

    plantList.innerHTML = "";

    if (!plants || plants.length === 0) {
        plantList.innerHTML = "<p>No plants found.</p>";
        return;
    }

    plants.forEach(plant => {

        const card = document.createElement("div");

        card.className = "plant-card";

        card.innerHTML = `
            <div class="plant-image">
                <img src="images/${slugify(plant.common_name)}.jpg"
                     alt="${plant.common_name}"
                     onerror="this.onerror=null;this.src='images/placeholder.jpg';">
            </div>

            <div class="plant-card-body">
                <h3>${plant.common_name}</h3>

                <p class="plant-scientific">
                    ${plant.scientific_name}
                </p>

                <p class="plant-family">
                    ${plant.family}
                </p>

                <p class="plant-description">
                    ${plant.description}
                </p>

                <button onclick="viewPlant(${plant.id})">
                    View Details
                </button>
            </div>
        `;

        plantList.appendChild(card);
    });
}


// GET ONE PLANT

async function viewPlant(id) {

    try {
        const plant = await fetchAPI(`/plants/${id}`);

        alert(`
Common Name:
${plant.common_name}

Scientific Name:
${plant.scientific_name}

Family:
${plant.family}

Genus:
${plant.genus}

Plant Type:
${plant.plant_type}

Origin:
${plant.origin}

Habitat:
${plant.habitat}

Lifespan:
${plant.lifespan}

Height M:
${plant.height_m} m

Spread M:
${plant.spread_m} m

Sunlight:
${plant.sunlight}

Water Requirement:
${plant.water_requirement}

Soil Type:
${plant.soil_type}

Flower Color:
${plant.flower_color}

Flowering Season:
${plant.flowering_season}

Uses:
${plant.uses}

Toxicity:
${plant.toxicity}

Description:
${plant.description}
        `);
    }

    catch (error) {
        console.error("Failed to retrieve plant:", error);

        alert("Unable to retrieve plant.");
    }
}


// SEARCH PLANTS

async function searchPlants() {

    const searchInput =
        document.getElementById("searchInput");

    const query = searchInput.value.trim();

    // Empty search = show everything
    if (!query) {
        loadPlants();
        return;
    }

    const plantList =
        document.getElementById("plantList");

    plantList.innerHTML = "<p>Searching...</p>";

    try {

        const data =
            await fetchAPI(
                `/plants/search?q=${encodeURIComponent(query)}`
            );

        displayPlants(data.results);

    }

    catch (error) {

        console.error("Search failed:", error);

        plantList.innerHTML =
            "<p>Search failed. Please try again.</p>";
    }
}


// START APPLICATION

loadPlants();

document
    .getElementById("searchInput")
    .addEventListener("keydown", function(event) {

        if (event.key === "Enter") {
            searchPlants();
        }

    });
