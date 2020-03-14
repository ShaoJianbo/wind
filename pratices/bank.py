from time import sleep
from threading import Thread, Lock


class Account():
    def __init__(self):
        self._balance = 0
        self.lock = Lock()

    def deposit(self, money):
        """存钱"""
        self.lock.acquire()  # 获得互斥锁
        try:
            new_balance = self._balance + money
            sleep(0.01)
            self._balance = new_balance
        finally:
            self.lock.release()

    @property
    def balance(self):
        return self._balance


class AddMoney(Thread):
    def __init__(self, account, money):
        super(AddMoney, self).__init__()
        self._account = account
        self._money = money

    def run(self):
        self._account.deposit(self._money)


def main():
    account = Account()
    threads = []
    for i in range(10):
        thread = AddMoney(account, 1)
        threads.append(thread)
        thread.start()

    for t in threads:
        t.join()

    print(f"account:->{account.balance}")


if __name__ == '__main__':
    main()
