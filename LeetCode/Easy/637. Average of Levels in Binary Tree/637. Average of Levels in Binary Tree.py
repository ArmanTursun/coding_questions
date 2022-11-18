# Easy

# Given the root of a binary tree, return the average value of the nodes on each level in the form of an array. Answers
# within 10-5 of the actual answer will be accepted.

# Example 1:
# Input: root = [3,9,20,null,null,15,7]
# Output: [3.00000,14.50000,11.00000]
# Explanation: The average value of nodes on level 0 is 3, on level 1 is 14.5, and on level 2 is 11.
# Hence return [3, 14.5, 11].

# Constraints:
# The number of nodes in the tree is in the range [1, 104].
# -231 <= Node.val <= 231 - 1

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        q = deque()
        q.append((root, 1))
        Level = 1
        result = []
        curSum = 0
        curNum = 0

        while q:
            curNode, curLevel = q.popleft()
            if curLevel != Level:
                result.append(round(curSum / curNum, 5))
                curSum = 0
                curNum = 0
                Level = curLevel
            curSum += curNode.val
            curNum += 1
            self.addChild(curNode, q, Level)
        result.append(round(curSum / curNum, 5))
        return result

    def addChild(self, node, q, Level):
        if node.left:
            q.append((node.left, Level + 1))
        if node.right:
            q.append((node.right, Level + 1))
## T = O(n); S = O(n)