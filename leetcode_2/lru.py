# 双向链表节点
class Node(object):
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        self.pre = None

    def get(self, key):
        return self.val


class LRUCache(object):
    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        # hash_map存储key-->Node 实现常熟级访问元素
        self.hash_map = dict()
        # 双向列表实现记录最近访问的元素-->首节点最新访问 尾节点最早访问
        self.head = Node("head", "head")
        self.tail = Node("tail", "tail")
        self.head.next = self.tail
        self.head.pre = self.tail
        self.tail.pre = self.head
        self.tail.next = self.head

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        res = self.hash_map.get(key, None)
        # print(res)
        if not res:
            return -1
        else:
            # 从列表中删除元素，并将访问的元素放到首位
            self.delete_node_from_list(key)
            self.add_node_to_head(key, res.val)
            return res.get(key)

    def delete_node_from_list(self, key):
        use_node = self.hash_map.get(key)
        pre_node = use_node.pre
        next_node = use_node.next
        next_node.pre = pre_node
        pre_node.next = next_node

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        # key不存在
        print("head-->", self.head.next.val, "tail-->", self.tail.pre.val)
        if self.get(key) == -1:
            if len(self.hash_map) == self.capacity:
                # 移除头部尾节点元素,新增元素到头节点
                self.delete_node_from_tail()
                # 新增元素到头节点
                self.add_node_to_head(key, value)
            else:
                # 新增元素到头节点
                self.add_node_to_head(key, value)

        # key存在
        else:
            # 更新元素的值
            if not self.get(key) == value:
                update_node = self.hash_map.get(key)
                update_node.val = value

            pass

    def delete_node_from_tail(self):
        delete_node = self.tail.pre
        self.tail.pre = delete_node.pre
        delete_node.pre.next = self.tail
        delete_node.next = None
        delete_node.pre = None
        del self.hash_map[delete_node.key]

    def add_node_to_head(self, key, value):
        new_node = Node(key, value)
        new_node.next = self.head.next
        new_node.pre = self.head
        self.head.next.pre = new_node
        self.head.next = new_node
        self.hash_map[key] = new_node


if __name__ == '__main__':
    # Your LRUCache object will be instantiated and called as such:
    capacity = 2
    cache = LRUCache(capacity)
    cache.put(1, 1)
    cache.put(1, 2)
    print(cache.get(1))
    cache.put(3, 3)

    print(cache.get(2))
    cache.put(4, 4)
    print(cache.get(1))
    print(cache.get(3))
    print(cache.get(4))
