# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # 基准条件:只有一个节点或是节点不存在返回
        if not head or not head.next:
            return head
        # 一般条件:将链表划分成两部分->分别排序->再合并
        head1 = head
        head2 = self.get_mid_node(head)
        if head2:
            print("head2 ==> {0}".format(head2.val))
        head1 = self.sortList(head1)
        head2 = self.sortList(head2)
        return self.merge_sort(head1, head2)

    @staticmethod
    def get_mid_node(head):
        if not head:
            return None

        pre = head
        slow = head.next
        fast = head.next
        while True:
            if fast:
                fast = fast.next
            else:
                break
            if fast:
                fast = fast.next
            else:
                break
            pre = slow
            slow = slow.next
        pre.next = None
        if slow:
            print("slow ==> {0}".format(slow.val))
        return slow

    @staticmethod
    def merge_sort(head1, head2):
        head = head3 = ListNode(-1)
        while head1 and head2:
            if head1.val > head2.val:
                head3.next = head2
                head2 = head2.next
            else:
                head3.next = head1
                head1 = head1.next
            head3 = head3.next
            head3.next = None

        if head1:
            head3.next = head1
        if head2:
            head3.next = head2
        return head.next

    @staticmethod
    def mergeTwoLists(head1, head2):
        """合并两个有序链表"""
        if not head1:
            return head2
        if not head2:
            return head1
        head_res = head3 = ListNode(-1)
        while head1 and head2:
            if head1.val < head2.val:
                head3.next = head1
                head1 = head1.next
            else:
                head3.next = head2
                head2 = head2.next
            head3 = head3.next
            head3.next = None

        if head1:
            head3.next = head1
        if head2:
            head3.next = head2
        return head_res.next


if __name__ == '__main__':
    # node1 = ListNode(4)
    # node2 = ListNode(2)
    # node3 = ListNode(1)
    # node4 = ListNode(3)
    # node1.next = node2
    # node2.next = node3
    # node3.next = node4
    #
    # so = Solution()
    # res = so.sortList(node1)
    # while res:
    #     print(res.val)
    #     res = res.next

    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(4)

    node1.next = node2
    node2.next = node3
    node3.next = None

    node4 = ListNode(1)
    node5 = ListNode(3)
    node6 = ListNode(4)

    node4.next = node5
    node5.next = node6
    node6.next = None

    so = Solution()
    res = so.mergeTwoLists(node1, node4)
    while res:
        print("{0}".format(res.val))
        res = res.next
