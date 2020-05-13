# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isSubStructure(self, A: TreeNode, B: TreeNode) -> bool:
        return bool(A and B) and (self.recur(A, B) or \
               self.isSubStructure(A.left, B) or \
               self.isSubStructure(A.right, B))

    def recur(self, A, B):
        """判断A树与B树是否一样"""
        # 当B节点为空->说明树B已经匹配完成
        if not B:
            return True
        # A节点为空->越过树A叶子节点->匹配失败
        # A与B的值不同->匹配失败
        if not A or A.val != B.val:
            return False
        return self.recur(A.left, B.left) and self.recur(A.right, B.right)


if __name__ == '__main__':
    so = Solution()
    n1 = TreeNode(1)
    n2 = TreeNode(2)
    n3 = TreeNode(3)
    n1.left = n2
    n1.right = n3

    n4 = TreeNode(1)
    n5 = TreeNode(2)
    n4.left = n5

    res = so.isSubStructure(n1, n4)
    print(res)
