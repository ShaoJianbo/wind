# coding:utf8
# 序列化二叉树的一种方法是使用前序遍历。当我们遇到一个非空节点时，
# 我们可以记录下这个节点的值。如果它是一个空节点，我们可以使用一个标记值记录，例如 #。
#
#      _9_
#     /   \
#    3     2
#   / \   / \
#  4   1  #  6
# / \ / \   / \
# # # # #   # #
# 例如，上面的二叉树可以被序列化为字符串 "9,3,4,#,#,1,#,#,2,#,6,#,#"，
# 其中 # 代表一个空节点。

# 给定一串以逗号分隔的序列，验证它是否是正确的二叉树的前序序列化。
# 编写一个在不重构树的条件下的可行算法。
# 每个以逗号分隔的字符或为一个整数或为一个表示 null 指针的 '#' 。
#
# 你可以认为输入格式总是有效的，例如它永远不会包含两个连续的逗号，比如 "1,,3" 。
# 示例 1:
#
# 输入: "9,3,4,#,#,1,#,#,2,#,6,#,#"
# 输出: true


# 读取到的结构只要符合二叉树性质而且不会在未读完之前就满足
# leaves = nodes + 1（完整的二叉树）即可
class Solution(object):
    def isValidSerialization(self, preorder):
        """
        :type preorder: str
        :rtype: bool
        """
        leaves = 0
        node = 0
        pres = preorder.split(",")
        for i, e in enumerate(pres):
            if e == '#':
                leaves += 1
            else:
                node += 1
            if leaves > node + 1:
                return False
            if leaves == node + 1 and i < len(pres) - 1:
                return False
        if leaves != node + 1:
            return False
        else:
            return True


if __name__ == '__main__':
    pre_order = "9,3,4,#,#,1,#,#,2,#,6,#,#"
    # pre_order = "1,#"
    # pre_order = "9,#,#,1"
    # pre_order = "1,#,#,#,#"
    # pre_order = "1,#,#,1"
    solution = Solution()
    res = solution.isValidSerialization(pre_order)
    print(res)
