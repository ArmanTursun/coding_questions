# Serialization is the process of converting a data structure or object into
# a sequence of bits so that it can be stored in a file or memory buffer,
# or transmitted across a network connection link to be reconstructed later
# in the same or another computer environment.

# Design an algorithm to serialize and deserialize a binary tree.
# There is no restriction on how your serialization/deserialization algorithm
# should work. You just need to ensure that a binary tree can be serialized
# to a string and this string can be deserialized to the original tree structure.

# Clarification: The input/output format is the same as how LeetCode serializes
# a binary tree. You do not necessarily need to follow this format, so please
# be creative and come up with different approaches yourself.


#          1
#         / \
#        2   3
#           / \
#          4   5
#
# Input: root = [1,2,3,null,null,4,5]
# Output: [1,2,3,null,null,4,5]

# Input: root = []
# Output: []


# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Codec:

    def serialize(self, root):
        def doit(node):
            if node:
                vals.append(str(node.val))
                doit(node.left)
                doit(node.right)
            else:
                vals.append('#')
        vals = []
        doit(root)
        return ' '.join(vals)

    def deserialize(self, data):
        def doit():
            val = next(vals)
            if val == '#':
                return None
            node = TreeNode(int(val))
            node.left = doit()
            node.right = doit()
            return node
        vals = iter(data.split())
        return doit()


class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        if not root: return ' '
        return ','.join([str(root.val), self.serialize(root.left), self.serialize(root.right)])

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        self.data = data
        # print (self.data)
        if self.data[0] == ' ': return None
        node = TreeNode(self.data[:self.data.find(',')])
        node.left = self.deserialize(self.data[self.data.find(',') + 1:])
        node.right = self.deserialize(self.data[self.data.find(',') + 1:])
        return node



    ###############################################################
    ###### Serialize to structure that consume minimum space ######
    ###############################################################

    from collections import deque
    class TreeNode:
        def __init__(self, val):
            self.val = val
            self.left = None
            self.right = None

    class TreeToArray:
        def __init__(self, root):
            self.root = root
            self.array = []
            self.array_sparse = []
            self.array_inorder = []

        def treetoarray_dense(self):
            height = self.getHeight(self.root)

            q = deque()
            q.append(self.root)
            count = 0

            while q:
                node = q.popleft()

                if not node:
                    if count < 2 ** height - 1:
                        self.array.append('#')
                        q.append(node)
                        q.append(node)
                        count += 1
                    continue

                self.array.append(node.val)
                q.append(node.left)
                q.append(node.right)
                count += 1

            return self.array

        def treetoarray_sparse(self):
            height = self.getHeight(self.root)

            q = deque()
            q.append(self.root)
            count = 0

            while q:
                node = q.popleft()

                if not node:
                    if count < 2 ** height - 1:
                        # self.array.append('#')
                        q.append(node)
                        q.append(node)
                        count += 1
                    continue

                self.array_sparse.append((node.val, count))
                q.append(node.left)
                q.append(node.right)
                count += 1

            return self.array_sparse

        def treetoarray_inorder(self):
            # height = self.getHeight(self.root)
            self.inorder(self.root, 0)
            return self.array_inorder

        def inorder(self, node, idx):
            if not node:
                return

                # self.array_inorder.append((node.val, idx))
            node_val = (node.val << 16) + idx
            self.array_inorder.append(node_val)
            # print (node_val >> 16, node_val & (2 ** 16 - 1))
            self.inorder(node.left, 2 * idx + 1)
            self.inorder(node.right, 2 * idx + 2)

        def getHeight(self, root):
            if not root:
                return 0
            return (max(self.getHeight(root.left), self.getHeight(root.right)) + 1)

        def buildTree(self, array):
            position = {}

            for item in array:
                val, idx = item >> 16, item & (2 ** 16 - 1)
                position[idx] = val

            # print(position)
            root = TreeNode(position[0])
            self.dfs_build(root, 0, position)
            return root

        def dfs_build(self, node, idx, position):
            if idx not in position:
                return
            # print (position[idx])
            if 2 * idx + 1 in position:
                node.left = TreeNode(position[2 * idx + 1])
                self.dfs_build(node.left, 2 * idx + 1, position)

            if 2 * idx + 2 in position:
                node.right = TreeNode(position[2 * idx + 2])
                self.dfs_build(node.right, 2 * idx + 2, position)

    def printall(root):
        if not root:
            return
        print(root.val)
        printall(root.left)
        printall(root.right)

    if __name__ == "__main__":
        #        n1               n1
        #       /  \             /  \
        #     n2   n3           n2   n3
        #     /    / \         / \  /   \
        #    n4   n5  n6     n4   # #    n5
        #                   /  \       /  \
        #                  #    #     #   n6

        n1 = TreeNode(1)
        n2 = TreeNode(2)
        n3 = TreeNode(3)
        n4 = TreeNode(4)
        n5 = TreeNode(5)
        n6 = TreeNode(6)
        '''
        n1.left = n2
        n1.right = n3
        n2.left = n4
        n3.left = n5
        n3.right = n6

        '''
        n1.left = n2
        n2.left = n4
        n1.right = n3
        n3.right = n5
        n5.right = n6

        q = TreeToArray(n1)
        # print(q.height)
        # print(q.treetoarray_dense())
        print(q.treetoarray_sparse())
        print(q.treetoarray_dense())
        array = q.treetoarray_inorder()
        print(array)
        root = q.buildTree(array)
        printall(root)

        # print(q.compressDenseTree(n1))
        # print(q.compressSparseTree(n1))
        # print(q.preorderAndInorder(n1))

    # [1, 2, 3, 4, None, None, 5, None, None, None, None, None, None, None, 6]
    # ([1, 2, 3, 4, 5, 6], [0, 1, 2, 3, 6, 14])
    # ([1, 2, 4, 3, 5, 6], [4, 2, 1, 3, 5, 6])