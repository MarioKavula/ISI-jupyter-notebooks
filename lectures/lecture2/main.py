from maze import Maze, Player

def dfs(maze, position, goal, visited):
    if position == goal:
        return [position]

    visited.add(position)
    possible_moves = maze.get_possible_moves(position)

    for move in possible_moves:
        new_x, new_y = position
        if move == "up":
            new_x -= 1
        elif move == "down":
            new_x += 1
        elif move == "left":
            new_y -= 1
        elif move == "right":
            new_y += 1

        new_position = (new_x, new_y)

        if new_position not in visited:
            path = dfs(maze, new_position, goal, visited)
            if path:
                return [position] + path

    return None

# Example usage
maze = Maze(20, 20)
maze.generate_maze()
start_position = maze.start_pos
end_position = maze.end_pos
visited = set()

path = dfs(maze, start_position, end_position, visited)

if path:
    print("Path found:", path)
    for pos in path:
        maze.mark_visited(pos)
else:
    print("No path found.")

maze.display()