const API_URL = "https://YOUR-API.vercel.app";


// GET ALL CARS
async function loadCars() {
    try {
        const response = await fetch(`${API_URL}/cars`);
        const data = await response.json();
        displayCars(data.cars);
    }

    catch (error) {
        console.error(error);
        document.getElementById("carList").innerHTML = "Unable to connect to the API.";
    }
}


// DISPLAY CARS
function displayCars(cars) {
    const carList =
        document.getElementById("carList");

    carList.innerHTML = "";

    cars.forEach(car => {
        const card = document.createElement("div");
        card.className = "car-card";
        card.innerHTML = `
            <div class="car-year">${car.year}</div>
            <h3>${car.make} ${car.model}</h3>
            <p class="car-engine">${car.engine}</p>
            <p>${car.horsepower} horsepower/p>
            <p>${car.description}</p>
            <button onclick="viewCar(${car.id})"> View Details</button>
        `;

        carList.appendChild(card);
    });

}

// GET ONE CAR
async function viewCar(id) {

    try {
        const response = await fetch(`${API_URL}/cars/${id}`);
        const car = await response.json();

        alert(`
            ${car.year} ${car.make} ${car.model}
            Engine:
            ${car.engine}

            Horsepower:
            ${car.horsepower}

            Description:
            ${car.description}
        `);
    }
    catch (error) {
        console.error(error);
        alert("Unable to retrieve car.");
    }

}

// SEARCH
async function searchCars() {

    const query = document.getElementById("searchInput").value;
    if (!query) {
        loadCars();
        return;
    }
    try {
        const response =
            await fetch(`${API_URL}/cars/search?q=${encodeURIComponent(query)}`);
        const data = await response.json();
        displayCars(data.results);
    }

    catch (error) {
        console.error(error);
        alert("Search failed.");
    }
}

loadCars();