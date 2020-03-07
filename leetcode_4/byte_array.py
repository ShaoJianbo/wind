# coding=utf-8


def fun(arr):
    max_n = max(arr)
    min_n = min(arr)
    arr_len = max_n - min_n
    arr_len = 122
    record = bytearray(arr_len + 1)
    print(record)


if __name__ == '__main__':
    arr = [0, 1, 10, 3, 4, -2111111122222]
    res = fun(arr)
    print(res)
