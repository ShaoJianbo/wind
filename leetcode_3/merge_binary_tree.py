# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:

        if not t1:
            return t2
        if not t2:
            return t1
        return self.merge_trees(t1, t2)

    def merge_trees(self, t1:TreeNode, t2:TreeNode)->TreeNode:
        if not t1:
            return t2
        if not t2:
            return t1
        # 采用中序遍历的方式合并
        node_value = t1.val + t2.val
        t = TreeNode(node_value)
        t.left = self.merge_trees(t1.left, t2.left)
        t.right = self.merge_trees(t1.right, t2.right)
        return t

