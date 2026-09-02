const API_URL = "https://ryokomet-cloudcomputing.vercel.app";

// FILTER CONFIGURATION (Dynamic & Scalable)
const FILTER_CONFIG = [
    { key: "genus", label: "Genus" },
    { key: "plant_type", label: "Plant Type" },
    { key: "origin", label: "Origin" },
    { key: "habitat", label: "Habitat" },
    { key: "lifespan", label: "Lifespan" },
    { key: "height_m", label: "Height", suffix: " m" },
    { key: "spread_m", label: "Spread", suffix: " m" },
    { key: "soil_type", label: "Soil Type" },
    { key: "flower_color", label: "Flower Color" },
    { key: "flowering_season", label: "Flowering Season" },
    { key: "uses", label: "Uses" },
    { key: "toxicity", label: "Toxicity" }
];

// Stores raw plants returned by loadPlants or searchPlants
let currentFetchedPlants = [];


// API REQUEST HELPER
async function fetchAPI(endpoint) {
    const response = await fetch(`${API_URL}${endpoint}`);

    if (!response.ok) {
        throw new Error(`API Error: ${response.status}`);
    }

    return await response.json();
}


// FILTER CONTROLS & DYNAMIC POPULATION

// Generate select dropdowns in the grid
function initFilterControls() {
    const grid = document.getElementById("filtersGrid");
    if (!grid) return;

    grid.innerHTML = FILTER_CONFIG.map(config => `
        <div class="filter-group">
            <label for="filter-${config.key}">${config.label}</label>
            <select id="filter-${config.key}" onchange="applyFilters()">
                <option value="">All ${config.label}s</option>
            </select>
        </div>
    `).join("");
}

// Extract unique values from loaded dataset and build options without duplicates
function populateFilterOptions(plants) {
    FILTER_CONFIG.forEach(config => {
        const select = document.getElementById(`filter-${config.key}`);
        if (!select) return;

        const currentValue = select.value;
        const uniqueValues = new Set();

        plants.forEach(plant => {
            const val = plant[config.key];
            if (val !== undefined && val !== null && val !== "") {
                // Split multi-item strings (e.g. uses: "Ornamental, Air purifying")
                if (typeof val === "string" && val.includes(",")) {
                    val.split(",").forEach(item => uniqueValues.add(item.trim()));
                } else {
                    uniqueValues.add(String(val).trim());
                }
            }
        });

        // Sort options numerically if numbers, alphabetically otherwise
        const sorted = Array.from(uniqueValues).sort((a, b) => {
            const numA = parseFloat(a);
            const numB = parseFloat(b);
            if (!isNaN(numA) && !isNaN(numB)) return numA - numB;
            return a.localeCompare(b);
        });

        select.innerHTML = `<option value="">All ${config.label}s</option>` +
            sorted.map(val => {
                const displayVal = config.suffix ? `${val}${config.suffix}` : val;
                return `<option value="${val}">${displayVal}</option>`;
            }).join("");

        // Preserve current selection if it still exists in dataset
        if (sorted.includes(currentValue)) {
            select.value = currentValue;
        }
    });
}

// Apply active drop-down filters to the current dataset
function applyFilters() {
    const filtered = currentFetchedPlants.filter(plant => {
        return FILTER_CONFIG.every(config => {
            const select = document.getElementById(`filter-${config.key}`);
            if (!select || !select.value) return true;

            const filterVal = select.value.toLowerCase();
            const plantVal = String(plant[config.key] || "").toLowerCase();

            return plantVal.includes(filterVal);
        });
    });

    displayPlants(filtered);
}

// Clear all active filter selections
function clearAllFilters() {
    FILTER_CONFIG.forEach(config => {
        const select = document.getElementById(`filter-${config.key}`);
        if (select) select.value = "";
    });
    applyFilters();
}


// GET ALL PLANTS
async function loadPlants() {
    const plantList = document.getElementById("plantList");
    plantList.innerHTML = "<p class=\"loading-text\">Loading plants...</p>";

    try {
        const data = await fetchAPI("/plants");
        currentFetchedPlants = data.plants || [];
        populateFilterOptions(currentFetchedPlants);
        applyFilters();
    } catch (error) {
        console.error("Failed to load plants:", error);
        plantList.innerHTML = "<p>Unable to connect to the API.</p>";
    }
}

// RESET SEARCH & RE-LOAD ALL
function resetAndLoadAll() {
    const searchInput = document.getElementById("searchInput");
    if (searchInput) searchInput.value = "";
    clearAllFilters();
    loadPlants();
}


// DISPLAY PLANTS
function slugify(text) {
    return text.toLowerCase().trim().replace(/\s+/g, '-');
}

function displayPlants(plants) {
    const plantList = document.getElementById("plantList");
    plantList.innerHTML = "";

    if (!plants || plants.length === 0) {
        plantList.innerHTML = "<p>No plants found matching your criteria.</p>";
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
    } catch (error) {
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

// Close modal on overlay click or Escape key
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
    const searchInput = document.getElementById("searchInput");
    const query = searchInput.value.trim();

    // Empty search = show everything
    if (!query) {
        loadPlants();
        return;
    }

    const plantList = document.getElementById("plantList");
    plantList.innerHTML = "<p class=\"loading-text\">Searching...</p>";

    try {
        const data = await fetchAPI(`/plants/search?q=${encodeURIComponent(query)}`);
        currentFetchedPlants = data.results || [];
        populateFilterOptions(currentFetchedPlants);
        applyFilters();
    } catch (error) {
        console.error("Search failed:", error);
        plantList.innerHTML = "<p>Search failed. Please try again.</p>";
    }
}


// START APPLICATION
initFilterControls();
loadPlants();

const searchInputEl = document.getElementById("searchInput");
if (searchInputEl) {
    searchInputEl.addEventListener("keydown", function(event) {
        if (event.key === "Enter") {
            searchPlants();
        }
    });
}