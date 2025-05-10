// // Carousel Logic
// const images = document.querySelectorAll('.carousel-image');
// const prevBtn = document.querySelector('.prev');
// const nextBtn = document.querySelector('.next');
// let currentIndex = 0;
// let interval;

// // Function to show the image at the current index
// function showImage(index) {
//     images.forEach((img, i) => {
//         img.classList.remove('active');
//         if (i === index) {
//             img.classList.add('active');
//         }
//     });
// }

// // Go to previous image
// prevBtn.addEventListener('click', () => {
//     currentIndex = (currentIndex - 1 + images.length) % images.length;
//     showImage(currentIndex);
//     resetInterval(); // reset timer after manual navigation
// });

// // Go to next image
// nextBtn.addEventListener('click', () => {
//     currentIndex = (currentIndex + 1) % images.length;
//     showImage(currentIndex);
//     resetInterval(); // reset timer after manual navigation
// });

// // Auto move to next image every 5 seconds
// function startAutoPlay() {
//     interval = setInterval(() => {
//         currentIndex = (currentIndex + 1) % images.length;
//         showImage(currentIndex);
//     }, 5000);
// }

// // Reset autoplay when user interacts
// function resetInterval() {
//     clearInterval(interval);
//     startAutoPlay();
// }

// // Initialize carousel
// showImage(currentIndex);
// startAutoPlay();

// // Live Date & Time
// function updateDateTime() {
//     const dateEl = document.getElementById('date');
//     const timeEl = document.getElementById('time');
//     const now = new Date();

//     const date = now.toLocaleDateString('en-CA'); // Format: YYYY-MM-DD
//     const time = now.toLocaleTimeString('en-GB'); // Format: HH:MM:SS

//     dateEl.textContent = `Current Date: ${date}`;
//     timeEl.textContent = `Time: ${time}`;
// }

// setInterval(updateDateTime, 1000);
// updateDateTime(); // run immediately

// // // --- New: Update Circle Colors ---
// // function updateCircleColors(temperature, humidity) {
// //     const tempBar = document.getElementById('temperature-bar');
// //     const humiBar = document.getElementById('humidity-bar');

// //     // Temperature color logic
// //     if (temperature < 20) { // Cold
// //         tempBar.style.borderColor = 'blue';
// //     } else { // Hot
// //         tempBar.style.borderColor = 'red';
// //     }

// //     // Humidity color logic
// //     if (humidity < 40) { // Dry
// //         humiBar.style.borderColor = 'blue';
// //     } else { // Wet
// //         humiBar.style.borderColor = 'red';
// //     }
// // }




// //  When user opens the page, Django sends latest temp/humidity.
// //  Every 3 seconds, JavaScript calls /api/sensor-data/
// //  Page updates Temperature and Humidity LIVE, without reload
// //  Smooth real-time dashboard effect like a professional IoT app
// // Every 3 seconds, page will auto-refresh only the sensor data

// // Live Sensor Data Fetch
// function fetchSensorData() {
//     fetch('/api/sensor-data/')
//     .then(response => response.json())
//     .then(data => {
//         document.getElementById('temperature').innerText = data.temperature + " °C";
//         document.getElementById('humidity').innerText = data.humidity + " %";
    
//         document.getElementById('temperature-value').innerText = data.temperature + "°C";
//         document.getElementById('humidity-value').innerText = data.humidity + "%";
    
//         updateCircleColors(data.temperature, data.humidity);
//     })
    
//     .catch(error => console.error('Error fetching sensor data:', error));
// }

// // Fetch data every 3 seconds
// setInterval(fetchSensorData, 3000);

// // Fetch immediately when page loads
// fetchSensorData();
// Carousel Logic









// Carousel
const images = document.querySelectorAll('.carousel-image');
const prevBtn = document.querySelector('.prev');
const nextBtn = document.querySelector('.next');
let currentIndex = 0;
let interval;

function showImage(index) {
    images.forEach((img, i) => {
        img.classList.toggle('active', i === index);
    });
}

prevBtn.addEventListener('click', () => {
    currentIndex = (currentIndex - 1 + images.length) % images.length;
    showImage(currentIndex);
    resetInterval();
});

nextBtn.addEventListener('click', () => {
    currentIndex = (currentIndex + 1) % images.length;
    showImage(currentIndex);
    resetInterval();
});

function startAutoPlay() {
    interval = setInterval(() => {
        currentIndex = (currentIndex + 1) % images.length;
        showImage(currentIndex);
    }, 5000);
}

function resetInterval() {
    clearInterval(interval);
    startAutoPlay();
}

showImage(currentIndex);
startAutoPlay();

// Date and Time
function updateDateTime() {
    const now = new Date();
    document.getElementById('date').textContent = `Current Date: ${now.toLocaleDateString('en-CA')}`;
    document.getElementById('time').textContent = `Time: ${now.toLocaleTimeString('en-GB')}`;
}

setInterval(updateDateTime, 1000);
updateDateTime();

// Map value to position (0-100 scale)
function mapValueToPosition(value, min, max) {
    return ((value - min) / (max - min)) * 100;
}

// Update bar point positions
function updateBars(temp, humi) {
    const tempPoint = document.getElementById('temp-point');
    const humiPoint = document.getElementById('humi-point');

    const tempPos = mapValueToPosition(temp, 0, 50); // Assuming temp 0-50°C
    const humiPos = mapValueToPosition(humi, 0, 100); // Assuming humidity 0-100%

    tempPoint.style.left = `${tempPos}%`;
    humiPoint.style.left = `${humiPos}%`;
}

// Fetch sensor data
function fetchSensorData() {
    fetch('/api/sensor-data/')
    .then(response => response.json())
    .then(data => {
        document.getElementById('temperature').innerText = data.temperature + " °C";
        document.getElementById('humidity').innerText = data.humidity + " %";

        updateBars(data.temperature, data.humidity);
    })
    .catch(error => console.error('Error fetching sensor data:', error));
}

setInterval(fetchSensorData, 3000);
fetchSensorData();













// graph or data visualization ki working
// Fetch old data for graphs
function fetchHistoryData() {
    fetch('/api/sensor-history/')
    .then(response => response.json())
    .then(data => {
        renderGraphs(data);
    })
    .catch(error => console.error('Error fetching history data:', error));
}

function renderGraphs(data) {
    // Temperature Line Graph
    new Chart(document.getElementById('tempLineChart'), {
        type: 'line',
        data: {
            labels: data.timestamps,
            datasets: [{
                label: 'Temperature (°C)',
                data: data.temperature,
                borderColor: 'red',
                backgroundColor: 'rgba(255, 99, 132, 0.2)',
                fill: true,
                tension: 0.4
            }]
        },
        options: {
            responsive: true,
            plugins: {
                legend: { position: 'top' },
                title: { display: true, text: 'Temperature Over Time' }
            }
        }
    });

    // Humidity Line Graph
    new Chart(document.getElementById('humiLineChart'), {
        type: 'line',
        data: {
            labels: data.timestamps,
            datasets: [{
                label: 'Humidity (%)',
                data: data.humidity,
                borderColor: 'blue',
                backgroundColor: 'rgba(54, 162, 235, 0.2)',
                fill: true,
                tension: 0.4
            }]
        },
        options: {
            responsive: true,
            plugins: {
                legend: { position: 'top' },
                title: { display: true, text: 'Humidity Over Time' }
            }
        }
    });
}

fetchHistoryData();






// --- Fetch Historical Sensor Data for Graphs ---
function fetchHistoryData() {
    fetch('/api/sensor-history/')
    .then(response => response.json())
    .then(data => {
        renderGraphs(data);
    })
    .catch(error => console.error('Error fetching history data:', error));
}

// --- Render Line Graphs using Chart.js ---
function renderGraphs(data) {
    // Temperature Line Graph
    new Chart(document.getElementById('tempLineChart'), {
        type: 'line',
        data: {
            labels: data.timestamps,
            datasets: [{
                label: 'Temperature (°C)',
                data: data.temperature,
                borderColor: 'red',
                backgroundColor: 'rgba(255, 99, 132, 0.2)',
                fill: true,
                tension: 0.4
            }]
        },
        options: {
            responsive: true,
            plugins: {
                legend: { position: 'top' },
                title: { display: true, text: 'Temperature Over Time' }
            }
        }
    });

    // Humidity Line Graph
    new Chart(document.getElementById('humiLineChart'), {
        type: 'line',
        data: {
            labels: data.timestamps,
            datasets: [{
                label: 'Humidity (%)',
                data: data.humidity,
                borderColor: 'blue',
                backgroundColor: 'rgba(54, 162, 235, 0.2)',
                fill: true,
                tension: 0.4
            }]
        },
        options: {
            responsive: true,
            plugins: {
                legend: { position: 'top' },
                title: { display: true, text: 'Humidity Over Time' }
            }
        }
    });
}

fetchHistoryData();
























    
