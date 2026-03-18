# 🗺️ Multimodal Route Planner

> **Graph-powered navigation engine** — optimal pathfinding across walking, bus, and metro networks using Dijkstra and A\*.

[![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=flat-square&logo=python&logoColor=white)](https://python.org)
[![Flask](https://img.shields.io/badge/Flask-REST%20API-000000?style=flat-square&logo=flask)](https://flask.palletsprojects.com)
[![Docker](https://img.shields.io/badge/Docker-ready-2496ED?style=flat-square&logo=docker&logoColor=white)](https://docker.com)
[![License: MIT](https://img.shields.io/badge/License-MIT-22c55e?style=flat-square)](LICENSE)

---

## What Is This?

A full-stack routing system that models a city's transit network as a weighted graph and computes optimal paths across multiple transport modes. Think of it as a simplified Google Maps backend — built from scratch to understand what's happening under the hood.

The project covers the full stack: graph construction, shortest-path algorithms, a REST API, an interactive map UI, and containerized deployment.

---

## ✨ Features

| Feature | Details |
|---|---|
| 🧭 Shortest path routing | Between any two nodes in the transit graph |
| 🚶 Multimodal transport | Walk, bus, and metro — with mode-aware edge weights |
| ⚡ Two algorithms | Dijkstra (exhaustive) and A\* (heuristic-guided) |
| 🌐 REST API | Built with Flask, returns JSON path data |
| 🗺️ Interactive map | Leaflet.js frontend with clickable route visualization |
| 🐳 Docker support | One-command build and run |

---

## 🧠 Algorithms

### Dijkstra's Algorithm
The classic. Explores all nodes in order of cumulative cost — guarantees the shortest path in any weighted graph with non-negative edges. Used here as the baseline.

- **Time complexity:** O((V + E) log V) with a priority queue
- **Best for:** Exhaustive search, verifying A\* correctness

### A\* (A-Star)
A smarter Dijkstra. Uses a heuristic function (Euclidean distance to the goal) to prioritize nodes that are *likely* on the optimal path, dramatically reducing unnecessary exploration.

- **Time complexity:** O(E log V) in practice, depending on heuristic quality
- **Best for:** Real-time routing where speed matters

> **When to use which?** A\* is almost always faster in practice. Dijkstra is useful when you need all-pairs shortest paths or don't have reliable coordinate data for a heuristic.

---

## 🏗️ Architecture

```
┌─────────────────────────────┐
│   Frontend (Leaflet + JS)   │  ← Click map to set start/end
└────────────┬────────────────┘
             │ HTTP GET /route?start=A&end=E&algo=astar
┌────────────▼────────────────┐
│      Flask REST API         │  ← Validates input, routes request
└────────────┬────────────────┘
             │
┌────────────▼────────────────┐
│   Graph Engine              │  ← Runs Dijkstra or A*
│   (algorithms.py)           │
└────────────┬────────────────┘
             │
┌────────────▼────────────────┐
│   Transit Graph             │  ← NetworkX graph from city_graph.json
│   (graph.py + JSON)         │
└─────────────────────────────┘
```

---

## 📂 Project Structure

```
multimodal-route-planner/
│
├── backend/
│   ├── app.py              # Flask API — endpoints and request handling
│   ├── graph.py            # Loads city_graph.json into a NetworkX graph
│   ├── algorithms.py       # Dijkstra and A* implementations
│   └── data/
│       └── city_graph.json # Nodes (stops) + edges (routes) with weights
│
├── frontend/
│   ├── index.html          # App shell
│   ├── map.js              # Leaflet map, click handlers, route rendering
│   └── styles.css          # UI styling
│
├── Dockerfile
├── requirements.txt
└── .gitignore
```

---

## ⚙️ Setup

### Option A — Local (Python)

**1. Clone the repository**
```bash
git clone https://github.com/<your-username>/multimodal-route-planner.git
cd multimodal-route-planner
```

**2. Install dependencies**
```bash
pip install -r requirements.txt
```

**3. Start the backend**
```bash
cd backend
python app.py
```

The server will be running at `http://127.0.0.1:5000`.

---

### Option B — Docker

**Build**
```bash
docker build -t route-planner .
```

**Run**
```bash
docker run -p 5000:5000 route-planner
```

---

## 🔌 API Reference

### `GET /route`

Compute the shortest path between two nodes.

| Parameter | Type | Required | Description |
|---|---|---|---|
| `start` | string | ✅ | Starting node ID (e.g. `"A"`) |
| `end` | string | ✅ | Destination node ID (e.g. `"E"`) |
| `algo` | string | ✅ | `dijkstra` or `astar` |

**Example request:**
```
GET http://127.0.0.1:5000/route?start=A&end=E&algo=astar
```

**Example response:**
```json
{
  "path": ["A", "B", "C", "D", "E"],
  "total_cost": 14.3,
  "algorithm": "astar",
  "nodes_explored": 4
}
```

> 💡 `nodes_explored` lets you compare how many nodes each algorithm visited for the same query — useful for understanding the A\* speedup.

---

## 📊 Performance Notes

Both algorithms use a **min-heap priority queue** (`heapq`) for O(log n) node selection. A\* reduces the effective search space using straight-line distance as the heuristic, which works well when geographic coordinates are available for each node.

On the sample city graph:
- Dijkstra explores all reachable nodes before terminating
- A\* typically explores 30–60% fewer nodes for the same query

For production-scale graphs (100k+ nodes), consider:
- Bidirectional A\*
- Contraction hierarchies
- Pre-computed landmark heuristics (ALT algorithm)

---

## 🔮 Roadmap

- [ ] Ingest real OpenStreetMap data via `osmnx`
- [ ] Time-dependent edge weights (rush hour, schedules)
- [ ] Bidirectional A\* for large graphs
- [ ] Real-time traffic layer via external API
- [ ] Algorithm benchmark dashboard (side-by-side comparison)
- [ ] Migrate backend to async FastAPI
- [ ] Mobile-responsive frontend

---

## 🤝 Contributing

Contributions welcome. To get started:

1. Fork the repo
2. Create a feature branch: `git checkout -b feature/your-feature`
3. Commit your changes: `git commit -m 'Add your feature'`
4. Push and open a pull request

For significant changes, please open an issue first to discuss scope.

---

## 📚 Further Reading

If you want to go deeper on the algorithms used:

- [Dijkstra's algorithm — original 1959 paper](https://doi.org/10.1007/BF01386390)
- [A\* search — Hart, Nilsson & Raphael (1968)](https://doi.org/10.1109/TSSC.1968.300136)
- [NetworkX documentation](https://networkx.org/documentation/stable/)
- [Leaflet.js documentation](https://leafletjs.com/reference.html)

---
