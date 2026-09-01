const API_URL = "https://ryokomet-cloudcomputing.vercel.app";

// ICONS

const ICON_SUN = `<svg viewBox="0 0 24 24" width="14" height="14" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"><circle cx="12" cy="12" r="4"></circle><path d="M12 2v3M12 19v3M4.2 4.2l2.1 2.1M17.7 17.7l2.1 2.1M2 12h3M19 12h3M4.2 19.8l2.1-2.1M17.7 6.3l2.1-2.1"/></svg>`;

const ICON_DROP = `<svg viewBox="0 0 24 24" width="14" height="14" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M12 3s6 7.2 6 11.2A6 6 0 0 1 6 14.2C6 10.2 12 3 12 3z"/></svg>`;


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

    plantList.innerHTML = "<p class=\"loading-text\">Loading plants...</p>";

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


// HELPERS

function slugify(text) {
    return text.toLowerCase().trim().replace(/\s+/g, '-');
}

function toxicityClass(text) {
    const t = (text || "").toLowerCase();
    if (t.includes("non-toxic")) return "tox-safe";
    if (t.includes("toxic")) return "tox-warn";
    return "";
}


// DISPLAY PLANTS

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
                <span class="plant-tag">${plant.family}</span>

                <h3>${plant.common_name}</h3>

                <p class="plant-scientific">
                    ${plant.scientific_name}
                </p>

                <div class="plant-meta">
                    <span class="meta-item"><span class="meta-icon">${ICON_SUN}</span>${plant.sunlight}</span>
                    <span class="meta-item"><span class="meta-icon">${ICON_DROP}</span>${plant.water_requirement}</span>
                </div>

                <p class="plant-description">
                    ${plant.description}
                </p>

                <button onclick="viewPlant(${plant.id})">
                    View details
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

        const modalImage = document.getElementById("modalImage");
        const modalContent = document.getElementById("modalContent");

        if (!modalImage || !modalContent) {
            console.error("Modal elements not found in the page.");
            return;
        }

        modalImage.src = `images/${slugify(plant.common_name)}.jpg`;
        modalImage.onerror = function() {
            this.onerror = null;
            this.src = "images/placeholder.jpg";
        };
        modalImage.alt = plant.common_name;

        modalContent.innerHTML = `
            <span class="plant-tag">${plant.family}</span>
            <h2>${plant.common_name}</h2>
            <p class="modal-scientific">${plant.scientific_name}</p>

            <div class="plant-meta modal-quickfacts">
                <span class="meta-item"><span class="meta-icon">${ICON_SUN}</span>${plant.sunlight}</span>
                <span class="meta-item"><span class="meta-icon">${ICON_DROP}</span>${plant.water_requirement}</span>
            </div>

            <div class="modal-row"><span>Genus</span><span>${plant.genus}</span></div>
            <div class="modal-row"><span>Plant type</span><span>${plant.plant_type}</span></div>
            <div class="modal-row"><span>Origin</span><span>${plant.origin}</span></div>
            <div class="modal-row"><span>Habitat</span><span>${plant.habitat}</span></div>
            <div class="modal-row"><span>Lifespan</span><span>${plant.lifespan}</span></div>
            <div class="modal-row"><span>Height</span><span>${plant.height_m} m</span></div>
            <div class="modal-row"><span>Spread</span><span>${plant.spread_m} m</span></div>
            <div class="modal-row"><span>Soil type</span><span>${plant.soil_type}</span></div>
            <div class="modal-row"><span>Flower color</span><span>${plant.flower_color}</span></div>
            <div class="modal-row"><span>Flowering season</span><span>${plant.flowering_season}</span></div>
            <div class="modal-row"><span>Uses</span><span>${plant.uses}</span></div>
            <div class="modal-row"><span>Toxicity</span><span class="${toxicityClass(plant.toxicity)}">${plant.toxicity}</span></div>

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
    const modal = document.getElementById("plantModal");
    if (modal) modal.classList.add("open");
}

function closeModal() {
    const modal = document.getElementById("plantModal");
    if (modal) modal.classList.remove("open");
}

// close modal on overlay click or Escape key
const plantModalEl = document.getElementById("plantModal");
if (plantModalEl) {
    plantModalEl.addEventListener("click", function(event) {
        if (event.target === this) closeModal();
    });
}

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

    plantList.innerHTML = "<p class=\"loading-text\">Searching...</p>";

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

const searchInputEl = document.getElementById("searchInput");
if (searchInputEl) {
    searchInputEl.addEventListener("keydown", function(event) {
        if (event.key === "Enter") {
            searchPlants();
        }
    });
}