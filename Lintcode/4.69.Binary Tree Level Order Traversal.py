#-*-coding:utf-8-*-
'''
Description
    Given a binary tree, return the level order traversal of its nodes' values.
    (ie, from left to right, level by level).

        The first data is the root node,
            followed by the value of the left and right son nodes,
            and "#" indicates that there is no child node.
        The number of nodes does not exceed 20.
'''
# Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

class Solution:
    """
    @param root: A Tree
    @return: Level order a list of lists of integer
    """

    def levelOrder(self, root):
        if root is None:
            return []

        result = []
        queue = [root]
        while len(queue) != 0:
            this_level = []
            next_level = []
            for node in queue:
                if node is not None:
                    this_level.append(node.val)
                    next_level.append(node.left)
                    next_level.append(node.right)
            if len(this_level) > 0:
                result.append(this_level)
            queue = next_level
        return result

    # 用一个队列的方法
    def levelOrder2(self, root):
        if root is None:
            return []
        queue = list([root])
        result = []
        while queue:
            level = []
            for _ in range(len(queue)):
                node = queue.pop(0)
                level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            result.append(level)
        return result

    # 用两个队列轮换方法
    def levelOrder3(self, root):
        if not root:
            return []

        queue = [root]
        results = []
        while queue:
            next_queue = []
            results.append([node.val for node in queue])
            for node in queue:
                if node.left:
                    next_queue.append(node.left)
                if node.right:
                    next_queue.append(node.right)
            queue = next_queue
        return results


s = Solution()
t = TreeNode(1)
t.left = TreeNode(2)
t.right = TreeNode(3)
print(s.levelOrder(t))
print(s.levelOrder2(t))
print(s.levelOrder3(t))
