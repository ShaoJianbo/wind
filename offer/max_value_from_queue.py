import sys


class Node(object):
    """利用双向链表的节点"""
    def __init__(self, val):
        self.val = val
        self.next = None
        self.pre = None


class MaxQueue(object):
    """链表实现最列"""
    def __init__(self):
        self.min_val = -sys.maxsize
        self.head = Node(self.min_val)
        self.tail = Node(self.min_val)
        self.head.next = self.tail
        self.head.pre = self.tail
        self.tail.pre = self.head
        self.tail.next = self.head
        self.max_node = None

    def max_value(self) -> int:
        """返回最大值"""
        if self.max_node:
            return self.max_node.val
        return -1

    def push_back(self, value: int) -> None:
        """入队"""
        new_node = Node(value)
        if self.head.next == self.tail:
            new_node.next = self.tail
            new_node.pre = self.head
            self.tail.pre = new_node
            self.head.next = new_node
        else:
            tail_node = self.tail.pre
            tail_node.next = new_node
            new_node.pre = tail_node
            new_node.next = self.tail
            self.tail.pre = new_node

        # 更新最大值节点
        if not self.max_node:
            self.max_node = new_node
        if self.max_node.val < value:
            self.max_node = new_node

    def pop_front(self) -> int:
        """出队"""
        # 空队列直接返回-1
        if self.head.next == self.tail:
            self.max_node = None
            return -1

        head_node = self.head.next
        next_node = head_node.next
        next_node.pre = self.head
        self.head.next = next_node

        if self.head.next == self.tail:
            self.max_node = None

        return head_node.val


if __name__ == "__main__":
    obj = MaxQueue()
    # ["MaxQueue","push_back","push_back","max_value","pop_front","max_value"]
    # [[],[1],[2],[],[],[]]
    # ["MaxQueue","max_value","pop_front","max_value","push_back","max_value",
    # "pop_front","max_value","pop_front","push_back","pop_front","pop_front",
    # "pop_front","push_back","pop_front","max_value","pop_front","max_value",
    # "push_back","push_back","max_value","push_back","max_value","max_value",
    # "max_value","push_back","pop_front","max_value","push_back","max_value",
    # "max_value","max_value","pop_front","push_back","push_back","push_back",
    # "push_back","pop_front","pop_front","max_value","pop_front","pop_front",
    obj.pop_front()
    print(obj.max_value())
    obj.push_back(1)
    obj.push_back(2)
    obj.pop_front()
    print(obj.max_value())
    print(obj.pop_front())
    print(obj.max_value())
