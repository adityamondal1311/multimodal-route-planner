var map = L.map('map').setView([20, 77], 5);

L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png')
.addTo(map);

async function getRoute() {

const res = await fetch(
"http://localhost:5000/route?start=A&end=E&algo=astar"
)

const data = await res.json()

console.log(data)

}