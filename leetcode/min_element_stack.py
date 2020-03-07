# coding:utf8


class MinStack(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.index = 0
        self.nums = [9999999] * 10000
        self.min_val = 10000000

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.nums[self.index] = x
        self.index += 1
        self.min_val = self.nums[0]
        for n in self.nums[1:self.index]:
            if self.min_val > n:
                self.min_val = n

    def pop(self):
        """
        :rtype: None
        """
        self.index -= 1
        self.min_val = self.nums[0]
        for n in self.nums[1:self.index]:
            if self.min_val > n:
                self.min_val = n

    def top(self):
        """
        :rtype: int
        """
        return self.nums[self.index - 1]

    def getMin(self):
        """
        :rtype: int
        """
        return self.min_val


if __name__ == '__main__':
    obj = MinStack()
    obj.push(-2)
    obj.push(0)
    obj.push(-3)
    print(obj.getMin())
    obj.pop()
    print(obj.index)
    print(obj.top())
    print(obj.index)
    print(obj.getMin())
