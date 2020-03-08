from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        # 建立前序数组的索引映射表,建立中序数组的索引映射表
        self.inorder_map = {key: val for val, key in enumerate(inorder)}
        self.preorder_map = {key: val for val, key in enumerate(preorder)}
        root = self.build_node(preorder, inorder)
        return root

    def build_node(self, preorder, inorder):
        """递归构建二叉树"""
        if not preorder or not inorder:
            return None

        root = TreeNode(preorder[0])
        root_idx = inorder.index(preorder[0])
        inorder_left = inorder[0:root_idx]
        inorder_right = inorder[root_idx + 1:]

        # 查找左节点的最大坐标
        preorder_left = preorder[1:root_idx + 1]
        preorder_right = preorder[root_idx + 1:]
        left_node = self.build_node(preorder_left, inorder_left)
        right_node = self.build_node(preorder_right, inorder_right)

        root.left = left_node
        root.right = right_node
        return root

    def buildTree1(self, preorder, inorder):
        """"""
        if len(inorder) == 0:
            return None
        # 前序遍历第一个值为根节点
        root = TreeNode(preorder[0])
        # 因为没有重复元素,所以可以直接根据值来查找根节点在中序遍历中的位置
        mid = inorder.index(preorder[0])
        # 构建左子树
        root.left = self.buildTree(preorder[1:mid + 1], inorder[:mid])
        # 构建右子树
        root.right = self.buildTree(preorder[mid + 1:], inorder[mid + 1:])

        return root

    def in_order(self, root):
        """中序遍历二叉树"""
        if not root:
            return
        # left = root.left
        self.in_order(root.left)
        print(root.val)
        self.in_order(root.right)


if __name__ == '__main__':
    so = Solution()
    preorder = [3, 9, 20, 15, 7]
    inorder = [9, 3, 15, 20, 7]
    res = so.buildTree(preorder, inorder)
    print(res)
    so.in_order(res)
