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
    distances = {(row, col): float('inf') for row in range(len(Board)) for col in range(len(Board[0]))}
    distances[Source] = 0
    prev = {(row, col): None for row in range(len(Board)) for col in range(len(Board[0]))}
    priority_queue = [(0, Source)]
    print(Board, Source, Destination)
    while priority_queue:
        dist, node = heapq.heappop(priority_queue)  # pop the node with the shortest distance
        for neighbor in find_neighbors(Board, node, distances):  # call neighbors function to find neighbors
            prev[neighbor] = node
            distances[neighbor] = dist + 1  # distance increases by 1 for each successive neighbor
            heapq.heappush(priority_queue, (distances[neighbor], neighbor))  # push the neighbor onto the queue
            if distances[Destination] != float('inf'):
                return find_path(prev, Destination)

    return []  # if no path possible


def find_neighbors(Board, Node, distances):
    """
    Finds the neighbors of a given node on the board. Movement is prioritized in the order of up, down, left, right.

    :param Board: The puzzle board from the parent function.
    :param Node: The node that is currently being processed by the parent function.
    :param distances: The dictionary which stores the distances from the parent function.
    :return: The neighboring nodes as a list of tuples.
    """
    neighbors = []
    row, col = Node
    # Must be in range of board, not a barrier, and not already visited
    if row > 0 and Board[row - 1][col] != '#' and distances[(row - 1, col)] == float('inf'):  # up
        neighbors.append((row - 1, col))
    if row < len(Board) - 1 and Board[row + 1][col] != '#' and distances[(row + 1, col)] == float('inf'):  # down
        neighbors.append((row + 1, col))
    if col > 0 and Board[row][col - 1] != '#' and distances[(row, col - 1)] == float('inf'):  # left
        neighbors.append((row, col - 1))
    if col < len(Board[0]) - 1 and Board[row][col + 1] != '#' and distances[(row, col + 1)] == float('inf'):  # right
        neighbors.append((row, col + 1))
    return neighbors


def find_path(prev, Destination):
    """
    Finds the path from the destination back to the source once we know the shortest path. Reverses the results
    to match the desired output.

    :param prev: The dictionary which stores the previous nodes from the parent function.
    :param Destination: The destination node.
    :return: A tuple containing the path traversed from the source to the destination and a string representing the
    path taken.
    """
    path_string = ''
    path = [Destination]  # list for the (reverse) path, starting with Destination
    current_node = Destination
    prev_node = prev[Destination]
    while prev_node is not None:  # source node has no previous node
        path.append(prev_node)  # adding the previous node
        if current_node[0] > prev_node[0]:  # 0 is the row, 1 is the column
            path_string += 'D'  # find which direction the next node is, and add the opposite of that to path and string
        elif current_node[0] < prev_node[0]:
            path_string += 'U'  # e.g. current node is above previous node, so we had to move up to get to current node
        elif current_node[1] > prev_node[1]:
            path_string += 'R'
        elif current_node[1] < prev_node[1]:
            path_string += 'L'
        current_node = prev_node
        prev_node = prev[prev_node]  # update pointers
    return path[::-1], path_string[::-1]  # path and string going back so reverse them


Puzzle = [
    ['-', '-', '-', '-', '-'],
    ['-', '-', '#', '-', '-'],
    ['-', '-', '-', '-', '-'],
    ['#', '-', '#', '#', '-'],
    ['-', '#', '-', '-', '-']
]

start = (4, 0)
end = (4, 4)
print(solve_puzzle(Puzzle, start, end))
# Output: [(0, 2), (0, 1), (1, 1), (2, 1), (2, 2)]
