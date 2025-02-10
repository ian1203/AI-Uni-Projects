# 🔍 Searches  

This directory contains two Python scripts that implement search algorithms for problem-solving in grid-based environments.


## 📜 Description of Scripts  

### 1️⃣ `treasure_on_island.py`  
This script implements a **Breadth-First Search (BFS)** algorithm to find the shortest path from a starting point to a treasure in a grid. The grid represents an island, where some cells may be obstacles.  

- 🏝 **Grid Representation**: A 2D list where `1` represents obstacles and `0` represents walkable paths.  
- 🔄 **Algorithm Used**: BFS (ensures shortest path in an unweighted grid).  
- 🎯 **Goal**: Find the minimum number of steps to reach the treasure.  

### 2️⃣ `city_network.py`  
This script models a **graph-based network** of cities and implements a **search algorithm** (possibly BFS or DFS) to find paths between cities.  

- 🏙 **Graph Representation**: A dictionary where nodes (cities) are connected by edges (roads).  
- 🔄 **Algorithm Used**: Graph traversal (DFS or BFS).  
- 🎯 **Goal**: Find the shortest or most efficient route between cities.  

## 🚀 How to Run the Scripts  

### 1️⃣ Clone the Repository  

```bash
git clone https://github.com/yourusername/AI-Uni-Projects.git
cd AI-Uni-Projects/Searches

python src/treasure_on_island.py
python src/city_network.py
