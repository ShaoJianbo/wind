# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getKthFromEnd(self, head: ListNode, k: int) -> ListNode:
        n = 0
        cur = head
        while cur:
            n += 1
            cur = cur.next

        k = n-k+1
        cur = head
        pre = head
        while k>0:
            cur = cur.next
            if k==1:
                pre = cur
            k -= 1
        pre.next = None
        return cur


if __name__ == '__main__':
    so = Solution()
    n1 = ListNode(1)
    n2 = ListNode(2)
    n3 = ListNode(3)
    n4 = ListNode(4)
    n5 = ListNode(5)

    n1.next = n2
    n2.next = n3
    n3.next = n4
    n4.next = n5

    k = 2
