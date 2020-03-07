class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    max_path = 0

    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        if not root:
            return 0
        self.dfs(root)
        return self.max_path -1

    def dfs(self, root):
        """计算某个节点的深度"""
        if not root:
            return 0
        left = self.dfs(root.left)
        right = self.dfs(root.right)
        self.max_path = max(self.max_path, left+right+1)
        return max(left, right) + 1



if __name__ == '__main__':
    n1 = TreeNode(1)
    n2 = TreeNode(2)
    n3 = TreeNode(3)
    n4 = TreeNode(4)
    n5 = TreeNode(5)
    n1.left = n2
    n1.right = n3
    n2.left = n4
    n2.right = n5

    so = Solution()
    res = so.diameterOfBinaryTree(n1)
    print(res)
    #
    # arr = [
    #     4, -7, -3, null, null, -9, -3, 9, -7, -4, null, 6, null, -6, -6, null,
    #     null, 0, 6, 5, null, 9, null, null, -1, -4, null, null, null, -2
    # ]
