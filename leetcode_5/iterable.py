class Iterator(object):
    def __init__(self, count=0):
        self.count = count
        self.start = 0

    def __iter__(self):
        """返回迭代器本身"""
        return self

    def __next__(self):
        """返回序列中的下一个项目"""
        if self.start <= self.count:
            temp = self.start
            self.start += 1
            return temp
        else:
            raise StopIteration


if __name__ == '__main__':
    it = Iterator(10)
    for i in it:
        print(i)
