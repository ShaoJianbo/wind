
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        l3 = ListNode(10)
        next_pos = 0
        cur_node = l3
        while l1 and l2:
            cur_num = l1.val + l2.val + next_pos
            cur_pos = cur_num - 10 if cur_num >= 10 else cur_num
            next_pos = 1 if cur_num >=10 else 0

            sum_node = ListNode(cur_pos)
            cur_node.next = sum_node
            cur_node = sum_node

            l1 = l1.next
            l2 = l2.next

        while l1:
            cur_num = l1.val + next_pos
            cur_pos = cur_num - 10 if cur_num >= 10 else cur_num
            next_pos = 1 if cur_num >= 10 else 0

            new_node = ListNode(cur_pos)
            cur_node.next = new_node
            cur_node = new_node
            l1 = l1.next

        while l2:
            cur_num = l2.val + next_pos
            cur_pos = cur_num - 10 if cur_num >= 10 else cur_num
            next_pos = 1 if cur_num >= 10 else 0

            new_node = ListNode(cur_pos)
            cur_node.next = new_node
            cur_node = new_node
            l2 = l2.next

        if next_pos:
            cur_node.next = ListNode(next_pos)

        return l3.next


if __name__ == '__main__':
    n1 = ListNode(9)
    # n2 = ListNode(8)
    # n3 = ListNode(3)
    # n1.next = n2
    # n2.next = n3

    n4 = ListNode(1)
    # n5 = ListNode(6)
    # n6 = ListNode(4)
    # n4.next = n5
    # n5.next = n6

    so = Solution()
    res = so.addTwoNumbers(n1, n4)
    while res:
        print(res.val)
        res = res.next
