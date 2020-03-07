# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        # 采用前序遍历的方式

        limit = [L, R]
        return self.pre_order(root, limit)

    def pre_order(self, node: TreeNode, limit) -> int:
        if not node:
            return 0
        else:
            if limit[0] <= node.val <= limit[1]:
                return self.pre_order(node.left, limit) + \
                       node.val + \
                       self.pre_order(node.right, limit)
            elif node.val < limit[0]:
                return self.pre_order(node.right, limit)
            elif node.val > limit[1]:
                return self.pre_order(node.left, limit)


if __name__ == '__main__':
    root = TreeNode(10)
    node1 = TreeNode(5)
    node2 = TreeNode(15)
    node3 = TreeNode(3)
    node4 = TreeNode(7)
    node5 = TreeNode(18)

    root.left = node1
    root.right = node2
    node1.left = node3
    node1.right = node4
    node2.right = node5

    L = 7
    R = 15
    so = Solution()
    res = so.rangeSumBST(root, L, R)
    print(res)
