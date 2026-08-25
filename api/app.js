const API_URL = "https://ryokomet-cloudcomputing.vercel.app";


// GET ALL TANKS
async function loadTanks() {
    try {
        const response = await fetch(`${API_URL}/tanks`);
        const data = await response.json();
        displayTanks(data.tanks);
    }

    catch (error) {
        console.error(error);
        document.getElementById("tankList").innerHTML = "Unable to connect to the API.";
    }
}


// DISPLAY TANKS
function displayTanks(tanks) {
    const tankList =
        document.getElementById("tankList");

    tankList.innerHTML = "";

    tanks.forEach(tank => {
        const card = document.createElement("div");
        card.className = "tank-card";
        card.innerHTML = `
            <div class="tank-year">${tank.year_introduced}</div>
            <h3>${tank.model} ${tank.model}</h3>
            <p class="tank-engine">${tank.engine}</p>
            <p>${tank.horsepower} horsepower/p>
            <p>${tank.description}</p>
            <button onclick="viewTank(${tank.id})"> View Details</button>
        `;

        tankList.appendChild(card);
    });

}

// GET ONE TANK
async function viewTank(id) {

    try {
        const response = await fetch(`${API_URL}/tanks/${id}`);
        const tank = await response.json();

        alert(`
            ${tank.year} ${tank.weight_tons} ${tank.model}
            Engine:
            ${tank.engine}

            Model:
            ${tank.model}

            Description:
            ${tank.description}
        `);
    }
    catch (error) {
        console.error(error);
        alert("Unable to retrieve tank.");
    }

}

// SEARCH
async function searchTanks() {

    const query = document.getElementById("searchInput").value;
    if (!query) {
        loadTanks();
        return;
    }
    try {
        const response =
            await fetch(`${API_URL}/tanks/search?q=${encodeURIComponent(query)}`);
        const data = await response.json();
        displayTanks(data.results);
    }

    catch (error) {
        console.error(error);
        alert("Search failed.");
    }
}

loadTanks();