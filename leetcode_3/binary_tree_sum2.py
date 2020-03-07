# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def convertBST(self, root: TreeNode) -> TreeNode:
        pre_list = self.pre_order(root)
        print(pre_list)
        self.add_right_tree(root, pre_list)
        return root

    def add_right_tree(self, node, pre_list):
        if not node:
            return
        else:
            node.val = sum(pre_list[pre_list.index(node.val):])
            self.add_right_tree(node.left, pre_list)
            self.add_right_tree(node.right, pre_list)

    def pre_order(self, node: TreeNode):
        if not node:
            return []
        else:
            left = self.pre_order(node.left)
            print("node.val->", node.val)
            right = self.pre_order(node.right)
            return left+[node.val] + right


def pre_order(node):
    if not node:
        return
    else:
        pre_order(node.left)
        print("node.val->", node.val)
        pre_order(node.right)
        return

if __name__ == '__main__':
    root = TreeNode(5)
    node1 = TreeNode(2)
    node2 = TreeNode(13)
    root.left = node1
    root.right = node2

    so = Solution()
    res = so.convertBST(root)
    print("RES----------->")
    pre_order(res)
    print(res)