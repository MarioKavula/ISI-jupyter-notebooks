import numpy as np
import matplotlib.pyplot as plt
import random

class Maze:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.grid = np.zeros((height, width), dtype=int)
        self.start_pos = (1, 1)
        self.end_pos = (height - 2, width - 2)
        self.visited = set()

    def generate_maze(self):
        self.grid.fill(1)
        x, y = self.start_pos
        self.grid[x][y] = 0
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

        self.grid[self.end_pos] = 0

    def mark_visited(self, pos):
        if self.grid[pos] == 0:
            self.visited.add(pos)

    def display(self, player_pos=None):
        cmap = plt.cm.Blues
        cmap.set_bad(color='red')

        masked_grid = np.ma.masked_where(self.grid == 0, self.grid)
        for pos in self.visited:
            if pos != self.start_pos and pos != self.end_pos:
                masked_grid[pos] = 0.5

        if player_pos:
            masked_grid[player_pos] = np.ma.masked

        plt.imshow(masked_grid, cmap=cmap, interpolation='none')
        plt.xticks([]), plt.yticks([])
        plt.show()

class Player:
    def __init__(self, start_pos):
        self.position = start_pos

    def move(self, direction, maze):
        x, y = self.position
        if direction == "up" and maze.grid[x - 1][y] == 0:
            self.position = (x - 1, y)
            maze.mark_visited(self.position)
        elif direction == "down" and maze.grid[x + 1][y] == 0:
            self.position = (x + 1, y)
            maze.mark_visited(self.position)
        elif direction == "left" and maze.grid[x][y - 1] == 0:
            self.position = (x, y - 1)
            maze.mark_visited(self.position)
        elif direction == "right" and maze.grid[x][y + 1] == 0:
            self.position = (x, y + 1)
            maze.mark_visited(self.position)
