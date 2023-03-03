# Name: James Wollenburg
# OSU Email: wollenbj@oregonstate.edu
# Course: CS325 - Analysis of Algorithms
# Assignment: Portfolio Project - Puzzle

import heapq


def solve_puzzle(Board, Source, Destination):
    """
    Solves the puzzle by finding the shortest path from the source to the destination. Uses Dijkstra's algorithm by
    assigning each edge a weight of 1 so that the shortest path is the path with the least number of edges.

    :param Board: A 2-d puzzle of size MxN filled with '-' representing empty spaces and '#' representing barriers.
    :param Source: The starting position of the puzzle. Given as a tuple: (a, b).
    :param Destination: The destination
    position of the puzzle. Given as a tuple: (x, y).
    :return: A list of tuples representing the shortest path from
    the source to the destination and a string representing the path as using R, L, D, U (right, left, down, up).
    """
    distances = {}
    for i in range(len(Board)):
        for j in range(len(Board[i])):
            distances[(i, j)] = float('inf')
    distances[Source] = 0
    priority_queue = [(0, Source)]
    path = []  # list of tuples representing the path from source to destination

    while priority_queue:
        break

    print(distances)
    return []  # if no path possible


Puzzle = [
    ['-', '-', '-', '-', '-'],
    ['-', '-', '#', '-', '-'],
    ['-', '-', '-', '-', '-'],
    ['#', '-', '#', '#', '-'],
    ['-', '#', '-', '-', '-']
]

start = (0, 2)
end = (2, 2)
print(solve_puzzle(Puzzle, start, end))
# Output: [(0, 2), (0, 1), (1, 1), (2, 1), (2, 2)]
