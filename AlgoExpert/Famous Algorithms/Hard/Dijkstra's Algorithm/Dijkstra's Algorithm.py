# Hard

# You're given an integer start and a list edges of pairs of integers.
# The list is what's called an adjacency list, and it represents a graph. The number of vertices in the
# graph is equal to the length of edges, where each index i in edges contains vertex i's outbound edges,
# in no particular order. Each individual edge is represented by an pair of two numbers, [destination,
# distance], where the destination is a positive integer denoting the destination vertex and the distance
# is a positive integer representing the length of the edge (the distance from vertex i to vertex destination).
# Note that these edges are directed, meaning that you can only travel from a particular vertex to its
# destination-not the other way around (unless the destination vertex itself has an outbound edge to the
# original vertex).

# Write a function that computes the lengths of the shortest paths between start and all of the other
# vertices in the graph using Dijkstra's algotithm and returns them in an array. Each index i in the
# output array should represent the length of the shortest path between start and vertex i. If no path
# is found from start to vertex i, then output[i] should be -1.

# Note that the graph represented by edges won't contain any self-loops.

# Sample Input
# start = 0
# edges = [
# [[1, 7]],
# [[2, 6], [3, 20], 4, 3],
# [3, 14],
# [4, 2],
# [],
# [],
# ]

# Sample Output
# [0, 7, 13, 27, 10, -1]

from heapq import heappush, heappop, heapify
def dijkstrasAlgorithm(start, edges):
    # Write your code here.
    visited = [-1 for i in range(len(edges))]
    visited[start] = 0
    hp = []
    heappush(hp, (0, start))
    while hp:
        curDistance, start = heappop(hp)
        for destination, distance in edges[start]:
            if visited[destination] == -1 or curDistance + distance < visited[destination]:
                visited[destination] = curDistance + distance
                heappush(hp, (curDistance + distance, destination))
    return visited

## T = O((v + e) * log(v)); O(v)
## If we use array instead of heap, then T = O(v ^ 2 + e)