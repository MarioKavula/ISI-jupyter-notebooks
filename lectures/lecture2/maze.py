import copy
import matplotlib as mpl
import numpy as np
import matplotlib.pyplot as plt
import random
import time
from IPython.display import clear_output

class Maze:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.grid = np.zeros((height, width), dtype=int)
        self.start_pos = (1, 1)
        self.end_pos = (height - 1, width - 1)
        self.visited = set()

    def generate_maze(self):
        self.grid.fill(1)  # Fill the maze with walls
        x, y = self.start_pos
        self.grid[x][y] = 0  # Mark the start position as a path
        stack = [(x, y)]

        while stack:
            cell = []
            if x + 2 < self.height - 1 and self.grid[x + 2][y] == 1:
                cell.append("down")
            if x - 2 > 0 and self.grid[x - 2][y] == 1:
                cell.append("up")
            if y + 2 < self.width - 1 and self.grid[x][y + 2] == 1:
                cell.append("right")
            if y - 2 > 0 and self.grid[x][y - 2] == 1:
                cell.append("left")

            if len(cell) > 0:
                cell_chosen = (random.choice(cell))

                if cell_chosen == "right":
                    self.grid[x][y + 1] = 0
                    self.grid[x][y + 2] = 0
                    y = y + 2
                elif cell_chosen == "left":
                    self.grid[x][y - 1] = 0
                    self.grid[x][y - 2] = 0
                    y = y - 2
                elif cell_chosen == "down":
                    self.grid[x + 1][y] = 0
                    self.grid[x + 2][y] = 0
                    x = x + 2
                elif cell_chosen == "up":
                    self.grid[x - 1][y] = 0
                    self.grid[x - 2][y] = 0
                    x = x - 2

                stack.append((x, y))
            else:
                x, y = stack.pop()

        self.end_pos = (x, y)  # Update the end position to the last cell visited
        self.grid[self.end_pos] = 0  # Ensure it's marked as a path
    
    def display(self, player_pos=None, pause_time=0.5):
        # Create a colormap for different elements in the maze
        import matplotlib as mpl
        cmap = mpl.colors.ListedColormap(['white', 'black', 'red', 'blue', 'green'])
        bounds = [0, 0.5, 1.5, 2.5, 3.5, 4]
        norm = mpl.colors.BoundaryNorm(bounds, cmap.N)

        # Create a copy of the grid to modify for display
        display_grid = np.copy(self.grid)
        for pos in self.visited:
            display_grid[pos] = 2  # Mark visited paths
        display_grid[self.start_pos] = 3  # Mark the start position
        display_grid[self.end_pos] = 4  # Mark the end position

        if player_pos:
            display_grid[player_pos] = 1  # Mark the player's position

        clear_output(wait=True)  # Clear the previous figure
        plt.imshow(display_grid, cmap=cmap, norm=norm)
        plt.xticks([]), plt.yticks([])
        plt.show()
        
        time.sleep(pause_time)  # Pause to visualize the step

    def mark_visited(self, pos):
        if self.grid[pos] == 0:
            self.visited.add(pos)
    
    def has_reached_goal(self, current_pos):
        return current_pos == self.end_pos

    def get_possible_moves(self, current_pos):
        x, y = current_pos
        possible_moves = []
        if x > 0 and self.grid[x - 1][y] == 0:  # up
            possible_moves.append("up")
        if x < self.height - 1 and self.grid[x + 1][y] == 0:  # down
            possible_moves.append("down")
        if y > 0 and self.grid[x][y - 1] == 0:  # left
            possible_moves.append("left")
        if y < self.width - 1 and self.grid[x][y + 1] == 0:  # right
            possible_moves.append("right")
        return possible_moves

    def move_player(self, player, direction):
        if self.is_move_valid(player.position, direction):
            player.move(direction, self)
        return player.position

    def is_move_valid(self, current_pos, direction):
        x, y = current_pos
        if direction == "up":
            return x > 0 and self.grid[x - 1][y] == 0
        elif direction == "down":
            return x < self.height - 1 and self.grid[x + 1][y] == 0
        elif direction == "left":
            return y > 0 and self.grid[x][y - 1] == 0
        elif direction == "right":
            return y < self.width - 1 and self.grid[x][y + 1] == 0
        return False

class Player:
    def __init__(self, start_pos):
        self.position = start_pos

    def move(self, direction, maze):
        x, y = self.position
        if maze.is_move_valid(self.position, direction):
            new_pos = {
                "up": (x - 1, y),
                "down": (x + 1, y),
                "left": (x, y - 1),
                "right": (x, y + 1)
            }[direction]
            self.position = new_pos
            maze.mark_visited(new_pos)