# Easy

# You are given a 2D integer array logs where each logs[i] = [birthi, deathi] indicates the birth and death years of the
# ith person.
#
# The population of some year x is the number of people alive during that year. The ith person is counted in year x's
# population if x is in the inclusive range [birthi, deathi - 1]. Note that the person is not counted in the year that they die.
#
# Return the earliest year with the maximum population.
#
#
#
# Example 1:
#
# Input: logs = [[1993,1999],[2000,2010]]
# Output: 1993
# Explanation: The maximum population is 1, and 1993 is the earliest year with this population.

# Constraints:
#
# 1 <= logs.length <= 100
# 1950 <= birthi < deathi <= 2050

class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        years = [0 for _ in range(101)]

        for birth, death in logs:
            years[birth - 1950] += 1
            years[death - 1950] -= 1

        population = 0
        maxPop = 0
        maxYear = 1950

        for i, curPop in enumerate(years):
            population += curPop
            if population > maxPop:
                maxPop = population
                maxYear = i + 1950

        return maxYear
## T = O(n); S = O(n)