import numpy as np
import matplotlib.pyplot as plt
from matplotlib import colors

# Define the maze as a NumPy array: 1 for walls, 0 for paths
maze = np.array([
    [1, 1, 1, 1, 1],
    [1, 0, 0, 0, 1],
    [1, 0, 1, 0, 1],
    [1, 0, 1, 0, 1],
    [1, 1, 1, 1, 1]
])

# Define a function to visualize the maze
def draw_maze(maze, visited=None):
    if visited is None:
        visited = []

    # Create a colormap for the maze
    cmap = colors.ListedColormap(['white', 'black', 'blue'])
    # Create a 'color' matrix
    color_matrix = np.zeros((maze.shape[0], maze.shape[1]), dtype=int)
    for row, col in visited:
        color_matrix[row, col] = 2  # Blue for visited cells
    
    # Assign 1 for walls and 0 for paths
    color_matrix[maze == 1] = 1

    plt.figure(figsize=(5, 5))
    plt.imshow(color_matrix, cmap=cmap)
    plt.xticks([]), plt.yticks([])  # Hide the axes ticks
    plt.show()

# Dummy function for path-finding, replace with actual path-finding
def find_path(maze, start, end):
    path = []
    visited = []
    stack = [start]
    
    while stack:
        current = stack.pop()
        if current == end:
            break
        visited.append(current)
        # ... (path-finding logic here, add new positions to stack) ...
        
        # Update the visualization
        draw_maze(maze, visited)
        plt.pause(0.5)  # Pause for half a second
        
    return path

# Start and end positions
start = (1, 1)
end = (3, 3)

# Visualize the path-finding
find_path(maze, start, end)