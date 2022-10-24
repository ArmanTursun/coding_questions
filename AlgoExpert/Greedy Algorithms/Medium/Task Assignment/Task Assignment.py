# Medium

# You're given an integer k representing a number  of workers and an array of positive integers representing
# durations of tasks that must be completed by the workers. Specifically, each worker must complete two unique
# tasks and can only work on one task at a time. The number of tasks will always be equal to 2k such that
# each worker always has exactly two tasks to complete. All tasks are independent of one another and can be
# completed in any order. Workers will complete their assigned tasks in parallel, and the time taken to complete
# all tasks will be equal to the time taken to complete the longest pair of tasks.

# Write a function that returns the optimal assignment of tasks to each worker such that the tasks to each
# worker such that the takss are completed as fast as possible. Your function should return a list of pairs,
# where each pair stores the indices of the tasks that should be completed by one worker. The pairs should
# be in the following format: [task1, task2], where the order of task1 and task2 doesn't matter. Your function
# can return the pairs in any order. If multiple optimal assignments exist, any corrent answer will be accepted.

# Sample Input
# k = 3
# tasks = [1, 3, 5, 3, 1, 4]

# Sample Output
# [[0, 2], [4, 5], [1, 3]]

from collections import defaultdict
def taskAssignment(k, tasks):
    # Write your code here.
    memo = defaultdict(list)
    for i in range(len(tasks)):
        memo[tasks[i]].append(i)
    tasks.sort()
    result = []
    left = 0
    right = len(tasks) - 1

    while left < right:
        result.append([memo[tasks[left]].pop(), memo[tasks[right]].pop()])
        left += 1
        right -= 1
    return result


def taskAssignment(k, tasks):
    # Write your code here.
    taskWithIdx = sorted(range(len(tasks)), key = lambda x : tasks[x])
    result = []
    for i in range(k):
        result.append([taskWithIdx[i], taskWithIdx[-i - 1]])
    return result


def taskAssignment(k, tasks):
    # Write your code here.
    taskWithIdx = sorted(enumerate(tasks), key = lambda x : x[1])
    result = []
    for i in range(k):
        result.append([taskWithIdx[i][0], taskWithIdx[-i - 1][0]])
    return result

## T = O(nlog(n)); S = O(n)