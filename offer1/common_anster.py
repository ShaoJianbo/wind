# Definition for a binary tree root.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lcaDeepestLeaves(self, root):
        ans, depth = self.get_depth(root)
        print(ans.val, depth)
        return ans

    def get_depth(self, root):
        """遍历node节点,根据左右子树的深度决定返回公共父节点"""
        if not root:
            return None, 0
        lr, ld = self.get_depth(root.left)
        rr, rd = self.get_depth(root.right)

        if ld > rd:
            return lr, ld+1
        elif ld < rd:
            return rr, rd+1
        else:
            return root, ld + 1


if __name__ == '__main__':
    so = Solution()
    n1 = TreeNode(1)
    n2 = TreeNode(2)
    n3 = TreeNode(3)
    n1.left = n2
    n1.right = n3

    res = so.lcaDeepestLeaves(n1)
    print(res)
