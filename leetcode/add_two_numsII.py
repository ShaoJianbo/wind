# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if not l1:
            return l2
        if not l2:
            return l1
        # 反转列表
        l1 = self.reverse_list(l1)
        l2 = self.reverse_list(l2)
        res = l3 = ListNode(0)
        next_val = 0
        while l1 and l2:
            sum_val = l1.val + l2.val + next_val
            # print("sum_val", sum_val)
            if sum_val >= 10:
                sum_val -= 10
                next_val = 1
            else:
                next_val = 0
            l3.next = ListNode(sum_val)
            l3 = l3.next
            l1 = l1.next
            l2 = l2.next

        if l1:
            pass
        elif l2:
            l1 = l2

        while l1:
            print("l1-->", l1.val, "next_val", next_val)
            sum_val = l1.val + next_val
            if sum_val >= 10:
                sum_val -= 10
                next_val = 1
            else:
                next_val = 0
            l3.next = ListNode(sum_val)
            l3 = l3.next
            l1 = l1.next

        if next_val > 0:
            l3.next = ListNode(next_val)
            l3 = l3.next
        return self.reverse_list(res.next)

    def reverse_list(self, l1):
        # 反转列表
        if not l1 or not l1.next:
            return l1
        pre = l1
        cur = l1.next
        pre.next = None
        while cur:
            final_node = cur.next
            cur.next = pre
            pre = cur
            cur = final_node

        return pre

    def addTwoNumbers_stack(self, l1, l2):
        # 双栈法
        if not l1:
            return l2
        if not l2:
            return l1
        stack1 = []
        stack2 = []
        while l1:
            stack1.append(l1)
            l1 = l1.next
        while l2:
            stack2.append(l2)
            l2 = l2.next
        stack3 = []
        next_sum = 0
        while stack1 and stack2:
            l1_node = stack1.pop()
            l2_node = stack2.pop()
            cur_sum = l1_node.val + l2_node.val + next_sum
            if cur_sum >= 10:
                cur_sum -= 10
                next_sum = 1
            else:
                next_sum = 0
            stack3.append(ListNode(cur_sum))

        if stack1:
            pass
        elif stack2:
            stack1 = stack2
        while stack1:
            l1_node = stack1.pop()
            cur_sum = l1_node.val + next_sum
            if cur_sum >= 10:
                cur_sum -= 10
                next_sum = 1
            else:
                next_sum = 0
            stack3.append(ListNode(cur_sum))

        res = l3 = ListNode(-1)

        if next_sum:
            stack3.append(ListNode(next_sum))
            next_sum = 0

        while stack3:
            l3.next = stack3.pop()
            l3 = l3.next

        return res.next


    def addTwoNumbers_add(self, l1, l2):
        # 补位法
        pass


if __name__ == '__main__':
    l11 = ListNode(5)
    l12 = ListNode(2)
    l13 = ListNode(4)
    l14 = ListNode(3)
    # l11.next = l12
    # l12.next = l13
    # l13.next = l14

    l21 = ListNode(5)
    l22 = ListNode(6)
    l23 = ListNode(4)

    # l21.next = l22
    # l22.next = l23

    so = Solution()
    res = so.addTwoNumbers_stack(l11, l21)
    while res:
        print("res-->", res.val)
        res = res.next

