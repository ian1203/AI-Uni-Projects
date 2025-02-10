from collections import deque

def bfs(grid, start, treasure):
    rows, cols = len(grid), len(grid[0])
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    queue = deque([(start[0], start[1], 0)])
    visited = set()
    visited.add((start[0], start[1]))

    while queue:
        x, y, steps = queue.popleft()

        if (x, y) == treasure:
            return steps

        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] != 1 and (nx, ny) not in visited:
                queue.append((nx, ny, steps + 1))
                visited.add((nx, ny))

    return -1

def dfs(grid, start, treasure):
    rows, cols = len(grid), len(grid[0])
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    stack = [(start[0], start[1], 0)]
    visited = set()
    visited.add((start[0], start[1]))

    while stack:
        x, y, steps = stack.pop()

        if (x, y) == treasure:
            return steps

        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] != 1 and (nx, ny) not in visited:
                stack.append((nx, ny, steps + 1))
                visited.add((nx, ny))

    return -1

grid = [
    [0, 0, 0, 1, 0],
    [0, 0, 0, 0, 0],
    [1, 1, 1, 1, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 1, 1]
]

start = (0, 0)
treasure = (4, 0)

print("BFS Shortest Path:", bfs(grid, start, treasure))
print("DFS Path Length (not guaranteed shortest):", dfs(grid, start, treasure))
