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

        document.getElementById("modalImage").src =
            `images/${slugify(plant.common_name)}.jpg`;
        document.getElementById("modalImage").onerror = function() {
            this.onerror = null;
            this.src = "images/placeholder.jpg";
        };
        document.getElementById("modalImage").alt = plant.common_name;

        document.getElementById("modalContent").innerHTML = `
            <h2>${plant.common_name}</h2>
            <p class="modal-scientific">${plant.scientific_name}</p>

            <div class="modal-row"><span>Family</span><span>${plant.family}</span></div>
            <div class="modal-row"><span>Genus</span><span>${plant.genus}</span></div>
            <div class="modal-row"><span>Plant Type</span><span>${plant.plant_type}</span></div>
            <div class="modal-row"><span>Origin</span><span>${plant.origin}</span></div>
            <div class="modal-row"><span>Habitat</span><span>${plant.habitat}</span></div>
            <div class="modal-row"><span>Lifespan</span><span>${plant.lifespan}</span></div>
            <div class="modal-row"><span>Height</span><span>${plant.height_m} m</span></div>
            <div class="modal-row"><span>Spread</span><span>${plant.spread_m} m</span></div>
            <div class="modal-row"><span>Sunlight</span><span>${plant.sunlight}</span></div>
            <div class="modal-row"><span>Water</span><span>${plant.water_requirement}</span></div>
            <div class="modal-row"><span>Soil Type</span><span>${plant.soil_type}</span></div>
            <div class="modal-row"><span>Flower Color</span><span>${plant.flower_color}</span></div>
            <div class="modal-row"><span>Flowering Season</span><span>${plant.flowering_season}</span></div>
            <div class="modal-row"><span>Uses</span><span>${plant.uses}</span></div>
            <div class="modal-row"><span>Toxicity</span><span>${plant.toxicity}</span></div>

            <p class="modal-description">${plant.description}</p>
        `;

        openModal();
    }

    catch (error) {
        console.error("Failed to retrieve plant:", error);
        alert("Unable to retrieve plant.");
    }
}

function openModal() {
    document.getElementById("plantModal").classList.add("open");
}

function closeModal() {
    document.getElementById("plantModal").classList.remove("open");
}

// close modal on overlay click or Escape key
document.getElementById("plantModal").addEventListener("click", function(event) {
    if (event.target === this) closeModal();
});

document.addEventListener("keydown", function(event) {
    if (event.key === "Escape") closeModal();
});


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
