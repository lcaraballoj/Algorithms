import numpy as np
import time
from sys import maxsize
from itertools import permutations

def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n-1)

# implementation of traveling Salesman Problem
def travellingSalesmanProblem(graph, cities, s):

    timeStart = time.time()
    # store all vertex apart from source vertex
    vertex = []
    for i in range(cities):
        if i != s:
            vertex.append(i)
    # store minimum weight Hamiltonian Cycle
    min_path = maxsize
    next_permutation=permutations(vertex)
    #l = list(permutations(range(1, cities)))
    for i in next_permutation:

        # store current Path weight(cost)
        current_pathweight = 0

        # compute current path weight
        k = s
        for j in i:
            current_pathweight += graph[k][j]
            k = j
        current_pathweight += graph[k][s]

        # update minimum
        min_path = min(min_path, current_pathweight)

        timeEnd = time.time()
        runTime = timeEnd - timeStart

    return min_path, runTime

def shortestPath(graph, s):
    shortestPath = []
    cities = len(graph)
    for i in range(1, cities):
        index = -1
        distance = float("inf")

        for j in range(cities):
            if j == s:
                continue

            newDistance = j
            if newDistance <= distance:
                index = j
                distance = newDistance
            shortestPath.append(index)
        shortestPath.append(s)
        shortestPath.reverse()

        return shortestPath

def insertValue(value):
    cities = row = column = value
    graph = np.random.randint(20, size=(row, column))
    s = 0

    print("Number of cities: {}\nGraph:\n{}\nMinimum Weight, Time: {}\n".format(cities, graph, travellingSalesmanProblem(graph, cities, s)))


def testCases():
    # Case 1, 6 cities
    # Will run in < .0004 seconds
    insertValue(6)

    # Case 2, 10 cities
    # Will run in < 1 second
    insertValue(10)

    # Case 3, 12 cities
    # Will run in < 140 seconds
    insertValue(12)

    # Case 4, 15 cities
    # Have to bail out
    insertValue(15)

    # Variable Test Case
    insertValue(input("How may cities?\n"))

testCases()
