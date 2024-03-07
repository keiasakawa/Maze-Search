import math
from queue import PriorityQueue

def reconstruct_path(cameFrom, current):
    total_path = [current]
    while current in cameFrom.keys():
        current = cameFrom[current]
        total_path.insert(0, current)

def heuristic(start, goal):
    return math.abs(start.x - goal.x) + math.abs(start.x - goal.x)


def a_star_algorithm(start, goal, maze):
    openSet = PriorityQueue()
    openSet.put((heuristic(start, goal), start))

    cameFrom = {}

    gScore = {}
    fScore = {}
    for x in range(len(maze)):
        for y in range(len(maze[0])):
            gScore[maze[x][y]] = math.inf
            fScore[maze[x][y]] = math.inf
    gScore[start] = 0
    fScore[start] = heuristic(start, goal)

    while not openSet:
        current = openSet.get()
        if current == goal:

