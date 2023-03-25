import numpy as np
import random
from maze_functions import *


def possible_moves(grid_width, grid_height, cell: (int, int)):
    moves = []

    for direction in [north, south, east, west]:
        new_cell = direction(cell)
        if 0 <= new_cell[0] < grid_width and 0 <= new_cell[1] < grid_height:
            moves.append(new_cell)

    return moves


def generate_maze():
    width = 10
    height = 10
    grid = np.zeros((width, height, 2), bool)

    # set the current cell to a random value
    current_cell = (random.randint(0, width - 1), random.randint(0, height - 1))

    # a grid to track if the cell has been visited
    visited = np.zeros((width, height), bool)
    unvisited_count = width * height

    visited[current_cell] = True
    unvisited_count -= 1

    while unvisited_count > 0:
        moves = possible_moves(width, height, current_cell)
        new_cell = random.choice(moves)

        if not visited[new_cell]:
            link_cells(grid, current_cell, new_cell)

            visited[new_cell] = True
            unvisited_count -= 1

        current_cell = new_cell

    draw_maze(grid)


generate_maze()
