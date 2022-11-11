# Hard

# You're fiven three inputs, all of which are instances of an Orgchart class that have a directReports property
# pointing to their direct reports (children). The first input is the top manager in an organizational chart, and the other
# two inputs are reports in the organizational chart. The two reports are guaranteed to be distinct.

# Write a function taht returns the lowest common manager to the two reports.

# Sample Input
# topManager = Node A
# reportOne = Node E
# reportTwo = Node I

#          A
#       /    \
#      B      C
#    /  \    / \
#   D    E  F   G
#  / \
# H   I

# Sample Output
# Node B

def getLowestCommonManager(topManager, reportOne, reportTwo):
    # Write your code here.

    if topManager == reportOne:
        return reportOne
    if topManager == reportTwo:
        return reportTwo

    if not topManager.directReports:
        return None

    getOne = getTwo = False
    for report in topManager.directReports:
        getFromSubTree = getLowestCommonManager(report, reportOne, reportTwo)
        if getFromSubTree == reportOne:
            getOne = True
        elif getFromSubTree == reportTwo:
            getTwo = True
        elif getFromSubTree is not None:
            return getFromSubTree
    if getOne and getTwo:
        return topManager
    elif getOne:
        return reportOne
    elif getTwo:
        return reportTwo
    else:
        return None

# This is an input class. Do not edit.
class OrgChart:
    def __init__(self, name):
        self.name = name
        self.directReports = []
## T = O(n); S = O(d)