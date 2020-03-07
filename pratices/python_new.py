from functools import lru_cache
import time


def python_new():
    user = "Mike"
    log_message = f'User {user} has logged in'
    print(log_message)


def fun(sentence: str = "1") -> bool:
    print(sentence)
    return True


@lru_cache(maxsize=512)
def fib(number: int) -> int:
    if number <= 1:
        return number
    return fib(number - 1) + fib(number - 2)


def fib1(n):
    if n <= 1:
        return n
    return fib1(n - 1) + fib(n - 2)


if __name__ == '__main__':
    # python_new()
    # start = time.time()
    # fib(400)
    # end = time.time()
    # print(end - start)

    start = time.time()
    fib1(400)
    end = time.time()
    print(end - start)
