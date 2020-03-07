# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def countNodes(self, root: TreeNode) -> int:
        # return self.count(root)
        if not root:
            return 0
        node_queue = [root]
        count = 0
        while node_queue:
            node = node_queue.pop()
            count += 1
            if node.left:
                node_queue.append(node.left)
            if node.right:
                node_queue.append(node.right)
        return count

    # def count(self, root: TreeNode) -> int:
    #     if not root:
    #         return 0
    #     left_count = self.count(root.left)
    #     right_count = self.count(root.right)
    #     return 1 + left_count + right_count


if __name__ == '__main__':
    so = Solution()
    root = TreeNode(1)
    n1 = TreeNode(2)
    n2 = TreeNode(3)
    root.left = n1
    root.right = n2
    res = so.countNodes(root)
    print(res)
