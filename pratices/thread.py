# coding:utf8
import time


class Public(object):
    def __init__(self, session):
        self.session = session


def unlock_mongodb(name, session):
    print("I'am {0} task".format(name))
    flag = True
    while True:
        print("UNLOCK_MONGODB wait...")
        database = yield flag  # 暂停,等待信号量
        print("database->", database)
        while database != "mongodb":
            continue
        print("session==>", session)
        print("I can UNLOCK {0} name:{1}".format(database, name))
        return


def lock_mongodb(name):
    print("I'am {0}".format(name))
    try:
        public = Public("session")
        c = unlock_mongodb("UNLOCK", public)  # 构建消费者对象,并开始
        c.next()  # 唤醒yield
        time.sleep(1)
        backup()
        print("product is {0}".format(name))
        c.send("mongodb")
    except StopIteration as ex:
        print("LOCK task is end, everything is OK")
        return
    except Exception as ex:
        raise ex


def backup(name="BACKUP"):
    print("I'm {0}".format(name))
    time.sleep(1)
    return


if __name__ == '__main__':
    lock_mongodb("LOCK_MONGODB")
    pass

