import random
import numpy as np
from cell import Cell

SIZE = 50

def check_neighbors(current, maze):
    unvisited = []

    # EDGE CASE: AT THE TOP
    if current.x != 0 and not maze[current.x - 1][current.y].visited:
        unvisited.append(maze[current.x - 1][current.y])
        
    # EDGE CASE: AT THE LEFT
    if current.y != 0 and not maze[current.x][current.y - 1].visited:
        unvisited.append(maze[current.x][current.y - 1])
    
    # EDGE CASE: AT THE BOTTOM
    if current.x != SIZE - 1 and not maze[current.x + 1][current.y].visited:
        unvisited.append(maze[current.x + 1][current.y])

    # EDGE CASE: AT THE RIGHT
    if current.y != SIZE - 1 and not maze[current.x][current.y + 1].visited:
        unvisited.append(maze[current.x][current.y + 1])

    return unvisited

def remove_walls(current, neighbor):

    dx, dy = current.x - neighbor.x, current.y - neighbor.y
    # Neighbor is above
    if dx == 1:
        current.walls['top'] = False
        neighbor.walls['bottom'] = False

    # Neighbor is below
    elif dx == -1:
        current.walls['bottom'] = False
        neighbor.walls['top'] = False

    # Neighbor is to the right
    elif dy == -1:
        current.walls['right'] = False
        neighbor.walls['left'] = False

    elif dy == 1:
        current.walls['left'] = False
        neighbor.walls['right'] = False



def maze_generation_algorithm(maze):
    stack = []
    maze[0][0].visited = True
    stack.append(maze[0][0])
    while stack != []:
        current = stack.pop(-1)
        unvisited = check_neighbors(current, maze)
        if unvisited:
            stack.append(current)
            chosen_neighbor = random.choice(unvisited)
            remove_walls(current, chosen_neighbor)
            chosen_neighbor.visited = True
            stack.append(chosen_neighbor)

def create_maze():
    maze = np.array([[Cell(x, y) for y in range(SIZE)] for x in range(SIZE)])
    maze_generation_algorithm(maze)
    print([[maze[x][y].walls for y in range(SIZE)] for x in range(SIZE)])
    return maze


if __name__ == "__main__":
    create_maze()