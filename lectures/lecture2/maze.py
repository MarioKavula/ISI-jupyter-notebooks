import copy
import matplotlib as mpl
import numpy as np
import random
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors

class Maze:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.grid = np.zeros((height, width), dtype=int)
        self.start_pos = (2, 2)
        self.end_pos = (height - 2, width - 2)
        self.visited = set()

    def generate_maze(self):
        self.grid.fill(1)  # Fill the maze with walls
        x, y = self.start_pos
        self.grid[x][y] = 0  # Mark the start position as a path
        stack = [(x, y)]

        while stack:
            x, y = stack[-1]  # Always work with the current position at the top of the stack
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
                cell_chosen = random.choice(cell)

                if cell_chosen == "right":
                    self.grid[x][y + 1] = 0
                    self.grid[x][y + 2] = 0
                    y += 2
                elif cell_chosen == "left":
                    self.grid[x][y - 1] = 0
                    self.grid[x][y - 2] = 0
                    y -= 2
                elif cell_chosen == "down":
                    self.grid[x + 1][y] = 0
                    self.grid[x + 2][y] = 0
                    x += 2
                elif cell_chosen == "up":
                    self.grid[x - 1][y] = 0
                    self.grid[x - 2][y] = 0
                    x -= 2

                stack.append((x, y))
            else:
                stack.pop()

        # Explicitly set the end position to the bottom-right corner
        self.end_pos = (self.height - 2, self.width - 2)
        self.grid[self.start_pos] = 0  # Optional: Ensure start_pos is always path
        self.grid[self.end_pos] = 0  # Ensure end_pos is always path
    
    def display(self, player_pos=None):
        # Create a new display grid
        display_grid = np.copy(self.grid)

        # Set default values: 0 for paths, 1 for walls
        display_grid[display_grid == 0] = 0  # Paths as white
        display_grid[display_grid == 1] = 1  # Walls as black

        # Mark visited positions
        for pos in self.visited:
            display_grid[pos] = 5  # Visited as red

        # Mark the player's position
        if player_pos:
            display_grid[player_pos] = 2  # Player as green

        # Mark the end position
        display_grid[self.end_pos] = 3  # End as blue

        # Create a colormap
        cmap = mcolors.ListedColormap(['white', 'black', 'red', 'green', 'blue'])
        bounds = [0, 1, 2, 3, 4, 5]
        norm = mcolors.BoundaryNorm(bounds, cmap.N)

        plt.imshow(display_grid, cmap=cmap, norm=norm)
        plt.xticks([]), plt.yticks([])
        plt.show()

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