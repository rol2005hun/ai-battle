def solve_maze(maze):
    """Solves a maze using Depth-First Search (DFS)."""

    def find_start(maze):
        for r in range(len(maze)):
            for c in range(len(maze[0])):
                if maze[r][c] == 'S':
                    return (r, c)
        return None

    def is_valid(row, col):
        return 0 <= row < len(maze) and 0 <= col < len(maze[0]) and maze[row][col] != '#' and maze[row][col] != 'X'

    def dfs(row, col, path):
        if maze[row][col] == 'E':
            return path

        maze[row][col] = 'X'  # Mark as visited (part of current path)
        path.append((row, col))

        for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:  # Explore adjacent cells
            new_row, new_col = row + dr, col + dc
            if is_valid(new_row, new_col):
                result = dfs(new_row, new_col, path)
                if result:
                    return result

        path.pop()  # Backtrack: remove from current path
        return None

    start = find_start(maze)
    if not start:
        return "No start point found."

    path = dfs(start[0], start[1], [])

    if path:
      # Create a visual representation of the maze with the path marked
        visual_maze = [list(row) for row in maze] # create a copy of the maze
        for r, c in path:
            if visual_maze[r][c] != 'S' and visual_maze[r][c] != 'E': # avoid overwriting S and E
                visual_maze[r][c] = 'X'
        return "\n".join(["".join(row) for row in visual_maze])
    else:
        return "No path found."



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

solution = solve_maze(maze)
print(solution)


maze2 = [
    "#######",
    "#S....#",
    "#.#####",
    "#.....#",
    "#####.#",
    "#...#.#",
    "###.E##"
]
solution2 = solve_maze(maze2)
print(solution2)

maze3 = [
    "#######",
    "#S....#",
    "#.####E",
    "#.....#",
    "###.#.#",
    "#...#.#",
    "#######"
]

solution3 = solve_maze(maze3)
print(solution3)