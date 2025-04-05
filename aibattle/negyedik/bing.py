from collections import deque
import matplotlib.pyplot as plt
import numpy as np

def print_maze(maze):
    for row in maze:
        print("".join(row))

def is_valid_move(maze, x, y, visited):
    rows, cols = len(maze), len(maze[0])
    return 0 <= x < rows and 0 <= y < cols and maze[x][y] != '#' and not visited[x][y]

def bfs(maze, start, end):
    rows, cols = len(maze), len(maze[0])
    visited = [[False for _ in range(cols)] for _ in range(rows)]
    queue = deque([(start[0], start[1], [])])
    visited[start[0]][start[1]] = True

    while queue:
        x, y, path = queue.popleft()
        path = path + [(x, y)]

        if (x, y) == end:
            return path

        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            if is_valid_move(maze, nx, ny, visited):
                visited[nx][ny] = True
                queue.append((nx, ny, path))

    return None

def solve_maze(maze):
    start, end = None, None

    for i in range(len(maze)):
        for j in range(len(maze[i])):
            if maze[i][j] == 'S':
                start = (i, j)
            elif maze[i][j] == 'E':
                end = (i, j)

    if not start or not end:
        return None

    path = bfs(maze, start, end)

    if not path:
        print("No path found")
        return

    for x, y in path:
        if maze[x][y] not in ('S', 'E'):
            maze[x][y] = 'X'

    print_maze(maze)

# Example input maze
maze = [
    ['#', '#', '#', '#', '#', '#', '#'],
    ['#', 'S', '.', '.', '.', '.', '#'],
    ['#', '.', '#', '#', '#', '#', '#'],
    ['#', '.', '.', '.', '.', '.', '#'],
    ['#', '#', '#', '.', '#', '.', '#'],
    ['#', '.', '.', '.', '#', '.', '#'],
    ['#', '#', '#', '.', 'E', '#', '#']
]

def plot_maze(maze, path):
    maze_grid = np.array([[1 if cell == '#' else 0 for cell in row] for row in maze])
    path_coords = np.array(path)
    
    plt.imshow(maze_grid, cmap='binary')
    if len(path_coords) > 0:
        plt.plot(path_coords[:, 1], path_coords[:, 0], 'r-', linewidth=2)  # Plot path in red
    plt.gca().invert_yaxis()
    plt.show()

def solve_maze_with_visualization(maze):
    start, end = None, None

    for i in range(len(maze)):
        for j in range(len(maze[i])):
            if maze[i][j] == 'S':
                start = (i, j)
            elif maze[i][j] == 'E':
                end = (i, j)

    if not start or not end:
        return None

    path = bfs(maze, start, end)

    if not path:
        print("No path found")
        return

    for x, y in path:
        if maze[x][y] not in ('S', 'E'):
            maze[x][y] = 'X'

    print_maze(maze)
    plot_maze(maze, path)

solve_maze(maze)
solve_maze_with_visualization(maze)