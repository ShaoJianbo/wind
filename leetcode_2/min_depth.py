# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return self.min_depth(root)

    def min_depth(self, root):
        if not root:
            return 0
        elif not root.left and not root.right:
            return 1
        elif not root.left and root.right:
            return self.min_depth(root.right) + 1
        elif root.left and not root.right:
            return self.min_depth(root.left) + 1
        left_depth = self.min_depth(root.left)
        right_depth = self.min_depth(root.right)
        return min(left_depth, right_depth) + 1

    def min_depth_(self, root):
        if not root:
            return 0
        stack = [(1, root)]
        depth = float('inf')
        while stack:
            cur_depth, cur_node = stack.pop()
            if not cur_node.left and not cur_node.right:
                depth = min(depth, cur_depth)
            children = [cur_node.left, cur_node.right]
            for child in children:
                if child:
                    stack.append((cur_depth+1, child))
        return depth