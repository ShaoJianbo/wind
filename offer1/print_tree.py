
from typing import List
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[int]:
        queue = []
        if root:
            queue.append(root)
        else:
            return []
        ans = []
        while queue:
            cur = queue.pop(0)
            ans.append(cur.val)
            if cur.left:
                queue.append(cur.left)
            if cur.right:
                queue.append(cur.right)
        # print(f"ans->{ans}")
        return ans


if __name__ == '__main__':
    so = Solution()
    n1 = TreeNode(3)
    n2 = TreeNode(9)
    n3 = TreeNode(20)
    n4 = TreeNode(15)
    n5 = TreeNode(7)
    n1.left = n2
    n1.right = n3
    n3.left = n4
    n3.right = n5

    res = so.levelOrder(n1)
    print(res)
