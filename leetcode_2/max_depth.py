# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        return self.max_depth(root)

    def max_depth(self, root):
        """递归解法"""
        if not root:
            return 0
        else:
            return max(self.max_depth(root.left), self.max_depth(
                root.right)) + 1

    def max_depth_ok(self, root):
        stack = []
        depth = 0
        if root:
            stack.append((1, root))
        while stack:
            cur_depth, node = stack.pop()
            depth = max(depth, cur_depth)
            if node.left:
                stack.append((cur_depth + 1, node.left))
            if node.right:
                stack.append((cur_depth + 1, node.right))

        return depth
