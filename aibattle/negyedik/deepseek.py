from collections import deque
import matplotlib.pyplot as plt
import numpy as np

def solve_maze(maze):
    """Solve the maze using BFS and return the path."""
    # Find the start and end positions
    start = None
    end = None
    for i in range(len(maze)):
        for j in range(len(maze[i])):
            if maze[i][j] == 'S':
                start = (i, j)
            elif maze[i][j] == 'E':
                end = (i, j)
    if not start or not end:
        return None  # No start or end found

    # Directions for moving up, down, left, right
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    # BFS setup
    queue = deque([(start, [start])])  # Queue stores (current_position, path)
    visited = set([start])

    while queue:
        (current, path) = queue.popleft()
        if current == end:
            return path  # Return the path if end is reached

        # Explore neighbors
        for direction in directions:
            next_row, next_col = current[0] + direction[0], current[1] + direction[1]
            next_pos = (next_row, next_col)

            # Check if the next position is valid and not visited
            if (
                0 <= next_row < len(maze)
                and 0 <= next_col < len(maze[0])
                and maze[next_row][next_col] != '#'
                and next_pos not in visited
            ):
                visited.add(next_pos)
                queue.append((next_pos, path + [next_pos]))

    return None  # No path found

def print_maze_with_path(maze, path):
    """Print the maze with the path marked by 'X'."""
    for i in range(len(maze)):
        row = list(maze[i])
        for j in range(len(row)):
            if (i, j) in path and maze[i][j] not in {'S', 'E'}:
                row[j] = 'X'
        print("".join(row))

def visualize_maze(maze, path):
    """Visualize the maze and the path using matplotlib."""
    maze_array = np.array([list(row) for row in maze])
    rows, cols = maze_array.shape

    # Create a plot
    fig, ax = plt.subplots()
    ax.set_xticks(np.arange(cols))
    ax.set_yticks(np.arange(rows))
    ax.grid(True)

    # Color the maze
    for i in range(rows):
        for j in range(cols):
            if maze_array[i, j] == '#':
                ax.fill_between([j, j + 1], rows - i - 1, rows - i, color='black')
            elif maze_array[i, j] == 'S':
                ax.fill_between([j, j + 1], rows - i - 1, rows - i, color='green')
            elif maze_array[i, j] == 'E':
                ax.fill_between([j, j + 1], rows - i - 1, rows - i, color='red')
            elif (i, j) in path:
                ax.fill_between([j, j + 1], rows - i - 1, rows - i, color='blue')

    plt.gca().invert_yaxis()
    plt.show()

# Example maze
maze = [
    "#######",
    "#S....#",
    "#.#####",
    "#.....#",
    "###.#.#",
    "#...#.#",
    "###.E##"
]

# Solve the maze
path = solve_maze(maze)

# Print the result
if path:
    print("Path found:")
    visualize_maze(maze, path)
else:
    print("No path exists.")