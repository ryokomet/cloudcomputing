const API_URL = "https://ryokomet-cloudcomputing.vercel.app";


// ================================
// API REQUEST HELPER
// ================================

async function fetchAPI(endpoint) {
    const response = await fetch(`${API_URL}${endpoint}`);

    if (!response.ok) {
        throw new Error(`API Error: ${response.status}`);
    }

    return await response.json();
}


// ================================
// GET ALL TANKS
// ================================

async function loadTanks() {
    const tankList = document.getElementById("tankList");

    tankList.innerHTML = "<p>Loading tanks...</p>";

    try {
        const data = await fetchAPI("/tanks");

        displayTanks(data.tanks);
    }

    catch (error) {
        console.error("Failed to load tanks:", error);

        tankList.innerHTML =
            "<p>Unable to connect to the API.</p>";
    }
}


// ================================
// DISPLAY TANKS
// ================================

function displayTanks(tanks) {
    const tankList = document.getElementById("tankList");

    tankList.innerHTML = "";

    if (!tanks || tanks.length === 0) {
        tankList.innerHTML = "<p>No tanks found.</p>";
        return;
    }

    tanks.forEach(tank => {

        const card = document.createElement("div");

        card.className = "tank-card";

        card.innerHTML = `
            <div class="tank-year">
                ${tank.year_introduced}
            </div>

            <h3>${tank.model}</h3>

            <p class="tank-country">
                ${tank.country}
            </p>

            <p class="tank-type">
                ${tank.type}
            </p>

            <p class="tank-engine">
                Engine: ${tank.engine}
            </p>

            <p>
                ${tank.horsepower} horsepower
            </p>

            <p>
                ${tank.description}
            </p>

            <button onclick="viewTank(${tank.id})">
                View Details
            </button>
        `;

        tankList.appendChild(card);
    });
}


// ================================
// GET ONE TANK
// ================================

async function viewTank(id) {

    try {
        const tank = await fetchAPI(`/tanks/${id}`);

        alert(`
${tank.year_introduced} ${tank.model}

Country:
${tank.country}

Manufacturer:
${tank.manufacturer}

Type:
${tank.type}

Weight:
${tank.weight_tons} tons

Crew:
${tank.crew}

Engine:
${tank.engine}

Horsepower:
${tank.horsepower}

Maximum Speed:
${tank.max_speed_kmh} km/h

Range:
${tank.range_km} km

Armor:
${tank.armor_type}

Description:
${tank.description}
        `);
    }

    catch (error) {
        console.error("Failed to retrieve tank:", error);

        alert("Unable to retrieve tank.");
    }
}


// ================================
// SEARCH TANKS
// ================================

async function searchTanks() {

    const searchInput =
        document.getElementById("searchInput");

    const query = searchInput.value.trim();

    // Empty search = show everything
    if (!query) {
        loadTanks();
        return;
    }

    const tankList =
        document.getElementById("tankList");

    tankList.innerHTML = "<p>Searching...</p>";

    try {

        const data =
            await fetchAPI(
                `/tanks/search?q=${encodeURIComponent(query)}`
            );

        displayTanks(data.results);

    }

    catch (error) {

        console.error("Search failed:", error);

        tankList.innerHTML =
            "<p>Search failed. Please try again.</p>";
    }
}


// ================================
// START APPLICATION
// ================================

loadTanks();

document
    .getElementById("searchInput")
    .addEventListener("keydown", function(event) {

        if (event.key === "Enter") {
            searchTanks();
        }

    });
