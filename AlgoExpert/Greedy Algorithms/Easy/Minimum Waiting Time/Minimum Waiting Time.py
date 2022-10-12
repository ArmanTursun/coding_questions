# Easy

# You're given a non-empty array of positive integers representing the amounts of
# time that specific queries take to execute. Only one query can be executed at a time,
# but the queries can be executed in any order.

# A query's waiting time is defined as the amount of time that it must wait before its
# execution starts.

# Write a function that returns the minimum amount of total waiting time for all of the queries.

# Sample Input
# queries = [3, 2, 1, 2, 6]

# Sample Output
# 17 = 1 + 3 + 5 + 8

# Use heap
from heapq import heapify, heappop

def minimumWaitingTime(queries):
    # Write your code here.
    heapify(queries)
    total_wait = 0
    next_wait = 0
    while queries:
        cur_last = heappop(queries)
        total_wait += next_wait
        next_wait += cur_last

    return total_wait

# Use sorting
def minimumWaitingTime(queries):
    # Write your code here.
    queries.sort()
    total_wait = 0
    next_wait = 0
    for cur_last in queries:
        total_wait += next_wait
        next_wait += cur_last
    return total_wait