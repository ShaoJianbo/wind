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
        """深度遍历root节点,根据左右子树的深度决定返回公共父节点"""
        if not root:
            return None, 0
        left_root, left_depth = self.get_depth(root.left)
        right_root, right_depth = self.get_depth(root.right)

        if left_depth > right_depth:
            return left_root, left_depth+1
        elif left_depth < right_depth:
            return right_root, right_depth+1
        else:
            return root, left_depth + 1


if __name__ == '__main__':
    so = Solution()
    n1 = TreeNode(1)
    n2 = TreeNode(2)
    n3 = TreeNode(3)
    n1.left = n2
    n1.right = n3

    res = so.lcaDeepestLeaves(n1)
    print(res)
