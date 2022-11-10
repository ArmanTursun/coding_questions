# Hard

# You're given a list of arbitrary jobs that need to be completed; these jobs are represented by distinct
# integers. You're also given a list of dependencies. A dependency is represented as a pair of jobs where the
# first job is a prerequisite of the second one. In other words, the second job depends on the first one; it
# can only be completed once the first job is completed.

# Write a function that takes in a list of jobs and a list of dependencies and returns a list containing a valid
# order in which the given jobs can be completed. If no such order exists, the function should return an empty array.

# Sample Input
# jobs = [1, 2, 3, 4]
# deps = [[1, 2], [1, 3], [3, 2], [4, 2], [4, 3]]

# Sample Output
# [1, 4, 3, 2] or [4, 1, 3, 2]

def topologicalSort(jobs, deps):
    # Write your code here.
    noDegrees = []  ## Save job with no prev job
    adjacentList = {job: [] for job in jobs}  ## Save adjacentList
    inDegrees = {job: 0 for job in jobs}  ## Save inDegrees of each job

    ## Create adjacentList based on deps
    for start, end in deps:
        adjacentList[start].append(end)
        inDegrees[end] += 1

    ## select start job which has zero inDegrees (no prev job)
    for job in inDegrees:
        if inDegrees[job] == 0:
            noDegrees.append(job)

    result = []
    while noDegrees:
        curJob = noDegrees.pop()
        result.append(curJob)
        nextJobList = adjacentList[curJob]
        for nextJob in nextJobList:
            inDegrees[nextJob] -= 1
            if inDegrees[nextJob] == 0:
                noDegrees.append(nextJob)
    return result if len(result) == len(jobs) else []
## T = O(v + e); S = O(V + e) where v is the number of jobs
## e is the number of deps
## Can also be done with DFS
## To be Updated