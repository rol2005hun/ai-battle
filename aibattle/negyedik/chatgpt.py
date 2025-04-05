from collections import deque

def find_start_end(maze):
    start, end = None, None
    for r in range(len(maze)):
        for c in range(len(maze[r])):
            if maze[r][c] == 'S':
                start = (r, c)
            elif maze[r][c] == 'E':
                end = (r, c)
    return start, end

def solve_maze(maze):
    start, end = find_start_end(maze)
    if not start or not end:
        return "Invalid maze: Missing start or end point."
    
    rows, cols = len(maze), len(maze[0])
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    queue = deque([(start, [])])
    visited = set()
    
    while queue:
        (r, c), path = queue.popleft()
        if (r, c) in visited:
            continue
        visited.add((r, c))
        path = path + [(r, c)]
        
        if (r, c) == end:
            return path
        
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and maze[nr][nc] in {'.', 'E'}:
                queue.append(((nr, nc), path))
    
    return "No path found."

def print_maze_with_path(maze, path):
    maze_copy = [row[:] for row in maze]
    for r, c in path:
        if maze_copy[r][c] not in {'S', 'E'}:
            maze_copy[r][c] = 'X'
    for row in maze_copy:
        print("".join(row))

# Example maze
maze = [
    list("#######"),
    list("#S....#"),
    list("#.#####"),
    list("#.....#"),
    list("###.#.#"),
    list("#...#.#"),
    list("###.E##")
]

solution = solve_maze(maze)
if isinstance(solution, list):
    print_maze_with_path(maze, solution)
else:
    print(solution)
