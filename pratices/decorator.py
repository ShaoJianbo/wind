import datetime


def log(func):
    def wrapper(*args, **kwargs):
        print("call func-->{0}".format(func.__name__))
        return func(*args, **kwargs)

    return wrapper


@log
def now():
    print(datetime.datetime.now())


if __name__ == '__main__':
    now()
    import json
    res = json.dumps({"hello": "你好"}, ensure_ascii=False)
    print(res)
