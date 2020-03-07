class MyNumbers(object):
    """迭代器"""
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __iter__(self):
        self.start = 1
        return self

    def __next__(self):
        n = self.start
        if n >= self.end:
            raise StopIteration
        self.start += 1
        return n


def fibonacci(n):
    first, second = 0, 1
    counter = 0
    while True:
        if counter >= n:
            exit(0)
        yield first
        first, second = second, first + second
        counter += 1


if __name__ == '__main__':
    my = MyNumbers(1, 20)
    # for i in my:
    #     print(i)
    # use = iter(my)
    # while True:
    #     try:
    #         print(next(use))
    #     except StopIteration as ex:
    #         print(ex)
    #         break

    fib = fibonacci(5)
    while True:
        try:
            print(next(fib), end="\n")
        except StopIteration:
            pass