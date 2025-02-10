import heapq

graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('D', 5), ('E', 2)],
    'C': [('F', 3), ('G', 4)],
    'D': [('H', 3)],
    'E': [('H', 6)],
    'F': [('I', 4)],
    'G': [('J', 2)],
    'H': [('I', 1)],
    'I': [('J', 2)],
    'J': []
}

heuristic = {
    'A': 7, 'B': 6, 'C': 3, 'D': 5, 'E': 4, 'F': 2, 'G': 1,
    'H': 3, 'I': 1, 'J': 0
}


def greedy_best_first_search(start, goal):
    open_list = [(heuristic[start], start)]  # Priority queue sorted by h(n)
    came_from = {start: None}

    while open_list:
        _, current = heapq.heappop(open_list)

        if current == goal:
            return reconstruct_path(came_from, goal)

        for neighbor, _ in graph[current]:
            if neighbor not in came_from:
                came_from[neighbor] = current
                heapq.heappush(open_list, (heuristic[neighbor], neighbor))

    return None  # No path found


def a_star_search(start, goal, graph_search=False):
    open_list = [(heuristic[start], 0, start)]  # Priority queue (f(n), g(n), node)
    came_from = {start: None}
    g_score = {start: 0}
    closed_set = set() if graph_search else None

    while open_list:
        _, g, current = heapq.heappop(open_list)

        if current == goal:
            return reconstruct_path(came_from, goal)

        if graph_search:
            closed_set.add(current)

        for neighbor, cost in graph[current]:
            tentative_g = g + cost

            if neighbor not in g_score or tentative_g < g_score[neighbor]:
                g_score[neighbor] = tentative_g
                f_score = tentative_g + heuristic[neighbor]
                came_from[neighbor] = current
                heapq.heappush(open_list, (f_score, tentative_g, neighbor))

            if graph_search and neighbor in closed_set:
                continue
    return None


def reconstruct_path(came_from, current):
    path = []
    while current:
        path.append(current)
        current = came_from[current]
    return path[::-1]


start, goal = 'A', 'J'
gbfs_path = greedy_best_first_search(start, goal)
astar_tree_path = a_star_search(start, goal, graph_search=False)
astar_graph_path = a_star_search(start, goal, graph_search=True)

print("Greedy Best-First Search Path:", gbfs_path)
print("A* Tree Search Path:", astar_tree_path)
print("A* Graph Search Path:", astar_graph_path)
