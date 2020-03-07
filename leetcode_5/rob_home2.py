# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # def rob(self, root: TreeNode) -> int:
    #     dp = {}
    #     return self.rob_root(root, dp)
    #
    # def rob_root(self, root, dp):
    #     if not root:
    #         dp[None] = 0
    #         return dp[root]
    #     # 计算抢劫root节点的收益
    #     rob_sum = root.val
    #     if root in dp:
    #         return dp[root]
    #     if root.left:
    #         rob_sum += self.rob_root(root.left.left,
    #                                  dp) if root.left.left else 0
    #         rob_sum += self.rob_root(root.left.right,
    #                                  dp) if root.left.right else 0
    #     if root.right:
    #         rob_sum += self.rob_root(root.right.left,
    #                                  dp) if root.right.left else 0
    #         rob_sum += self.rob_root(root.right.right,
    #                                  dp) if root.right.right else 0
    #     # 计算不抢劫root节点的收益
    #     no_rob_sum = self.rob_root(root.left, dp) + self.rob_root(
    #         root.right, dp)
    #     dp[root] = max(rob_sum, no_rob_sum)
    #     return dp[root]

    def rob(self, root):
        return max(self.rob_home(root))

    def rob_home(self, root):
        # rob_arr[0]记录抢劫根节点的钱
        # rob_arr[1]记录不抢劫根节点的钱
        if not root:
            return [0, 0]
        left = self.rob_home(root.left)
        right = self.rob_home(root.right)
        rob_sum = root.val + left[1] + right[1]
        no_rob_sum = max(left[0],left[1]) + max(right[0],right[1])
        return [rob_sum, no_rob_sum]


if __name__ == '__main__':
    so = Solution()
    n1 = TreeNode(3)
    n2 = TreeNode(2)
    n3 = TreeNode(3)
    # n4 = TreeNode(3)
    n5 = TreeNode(3)
    # n6 = TreeNode(3)
    n7 = TreeNode(1)
    n1.left = n2
    n1.right = n3
    n2.right = n5
    n3.right = n7

    res = so.rob(n1)
    print(res)
