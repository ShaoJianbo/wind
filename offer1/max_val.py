class Node(object):
    def __init__(self, val):
        self.val = val
        self.pre = None
        self.next = None


class MaxQueue:
    def __init__(self):
        """实现双端队列"""
        self.head = Node("head")
        self.tail = Node("tail")
        self.head.next = self.tail
        self.head.pre = self.tail
        self.tail.next = self.head
        self.tail.pre = self.head
        self.max = None

    def max_value(self) -> int:
        return self.max.val if self.max else -1

    def push_back(self, value: int) -> None:
        """在队列的尾部插入节点"""
        new_node = Node(value)
        new_node.pre = self.tail.pre
        new_node.next = self.tail

        cur_tail_node = self.tail.pre
        cur_tail_node.next = new_node
        self.tail.pre = new_node

        if self.max:
            if self.max.val < value:
                self.max = new_node
        else:
            self.max = new_node

    def pop_front(self) -> int:
        """将队列头部的元素推出"""
        if self.head.next == self.tail:
            return -1
        head_node = self.head.next
        # head_node.pre = None
        # head_node.next = None
        self.head.next = head_node.next
        self.head.next.pre = self.head

        if self.max == head_node:
            cur = self.head.next
            self.max = None
            max_val = -float('Inf')
            while cur != self.tail:
                if cur.val >= max_val:
                    max_val = cur.val
                    self.max = cur
                cur = cur.next
        return head_node.val
