class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        res = []
        if not root:
            return res

        stack = [(1, root)]
        while stack:
            cur_depth, cur_node = stack.pop()
            # print("cur_depth==>", cur_depth, "res==>", res, "cur_node==>",
            #       cur_node.val)
            if cur_depth <= len(res):
                res[cur_depth - 1].insert(0, cur_node.val)
            else:
                res.append([cur_node.val])
            # print("res==>", res)
            children = [cur_node.left, cur_node.right]
            for child in children:
                if child:
                    stack.append((cur_depth + 1, child))
        return res

    def levelOrder1(self, root):
        # 递归访问树
        res = []

        if not root:
            return res

        def level_helper(node, level):
            if len(res) <= level:
                res.append([])
            res[level].append(node.val)
            if node.left:
                level_helper(node.left, level + 1)
            if node.right:
                level_helper(node.right, level + 1)

        level_helper(root, 0)
        return res


if __name__ == '__main__':
    node1 = TreeNode(3)
    node2 = TreeNode(9)
    node3 = TreeNode(20)
    node4 = TreeNode(15)
    node5 = TreeNode(7)
    node1.left = node2
    node1.right = node3
    node3.left = node4
    node3.right = node5

    so = Solution()
    res = so.levelOrder(node1)
    print(res)

    print("-------------")
    res = so.levelOrder1(node1)
    print(res)
