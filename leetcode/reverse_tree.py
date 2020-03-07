class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root or (root.left is None and root.right is None):
            return root
        left = self.invertTree(root.right)
        right = self.invertTree(root.left)
        root.left = left
        root.right = right
        return root


if __name__ == '__main__':
    node1 = TreeNode(4)
    node2 = TreeNode(7)
    node3 = TreeNode(2)
    node1.left = node2
    node1.right = node3

    so = Solution()
    root = so.invertTree(node1)
    print(root.left.val)
    print(root.right.val)
