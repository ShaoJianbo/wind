class CQueue:

    def __init__(self):
        self.stack1 = []
        self.stack2 = []


    def appendTail(self, value: int) -> None:
        """入队操作就是将元素全部放在stack1里面"""
        self.stack1.append(value)
        return


    def deleteHead(self) -> int:
        """删除队队头元素就是将stack1的元素全部倒出来
        放到stack2中，然后stack2中弹出元素；之后再将stack2中的元素全部
        放回"""
        if not self.stack1:
            return -1
        while self.stack1:
            n = self.stack1.pop()
            self.stack2.append(n)

        # print("-----------")
        # print(self.stack1)
        # print(self.stack2)
        top = self.stack2.pop()
        # print(self.stack1)
        # print(self.stack2)
        # print("-----------")
        # 放回元素
        while self.stack2:
            n = self.stack2.pop()
            self.stack1.append(n)

        # print("res->", top)
        return top

# Your CQueue object will be instantiated and called as such:
# obj = CQueue()
# obj.appendTail(value)
# param_2 = obj.deleteHead()

if __name__ == '__main__':
    so = CQueue()
    so.appendTail(5)
    so.appendTail(2)
    so.deleteHead()
    so.deleteHead()
