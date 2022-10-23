# Medium

# You're given a list of edges representing an unweighted, directed graph with at least one node. Write a function that
# returns a boolean representing whether the given graph contains a cycle.

# For the purpose of this question, a cycle is difined as any number of vertices, including just one vertex, that are
# connected in a closed chain. The given list is what's called an adjacency list, and it representd a grogh. The number
# of vertices in the graph is equal to the length of edges, where each index i in edges contains vertex i's outbound
# edges, in no particular order. Each individual edge is represented by a positive integer that denotes an index in the
# list that this vertex is connected to. Note that these edges are directed, meaning that you can only travel from a particular
# vertex to its destination, not the other way around.

# Also note that this graph may contain self-loops.

# Sample Input
# edges = [
#   [1, 3],
#   [2, 3, 4],
#   [0],
#   [],
#   [2, 5],
#   [] ]

# Sample Output
# True

def cycleInGraph(edges):
    # Write your code here.
    visited = [False for edge in edges]
    for i in range(len(edges)):
        if checkCycle(visited, i, edges):
            return True
    return False

def checkCycle(visited, i, edges):
    if visited[i]:
        return True
    visited[i] = True
    for next in edges[i]:
        if checkCycle(visited, next, edges):
            return True
    visited[i] = False
    return False

# T = O(v!); S = O(v)



def cycleInGraph(edges):
    # Write your code here.
    visited = [False for edge in edges]
    cur_path = [False for edge in edges]
    for i in range(len(edges)):
        if checkCycle(visited, i, edges, cur_path):
            return True
    return False

def checkCycle(visited, i, edges, cur_path):
    if visited[i] and cur_path[i]:
        return True
    visited[i] = True
    cur_path[i] = True
    for next in edges[i]:
        if checkCycle(visited, next, edges, cur_path):
            return True
    cur_path[i] = False
    return False

# T = O(v+e); S = O(v)



def cycleInGraph(edges):
    # Write your code here.
    visited = [0 for edge in edges]
    for i in range(len(edges)):
        if checkCycle(visited, i, edges):
            return True
    return False

def checkCycle(visited, i, edges):
    if visited[i] == 2:
        return True
    visited[i] = 2
    for next in edges[i]:
        if checkCycle(visited, next, edges):
            return True
    visited[i] = 1
    return False

# T = O(v+e); S = O(v)



