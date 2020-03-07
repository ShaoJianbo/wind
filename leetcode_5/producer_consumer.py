# -*- coding: utf-8 -*-
from threading import Thread
import uuid
import time

container = []  # 假定5个元素就满了


class Product():
    def __init__(self, id=None):
        if not id:
            self.id = uuid.uuid1()


class Producer(Thread):
    def __init__(self, name="", product_num=1):
        super(Producer, self).__init__()
        self.name = name
        self.product_num = product_num

    def run(self):
        while True:
            if len(container) <= 4:
                i = 0
                while i < self.product_num:
                    product = Product()
                    container.append(product)
                    print("make product->", product.id)
                    i += 1
                time.sleep(1)  # 休息1s
            else:
                print("container is full, waiting...")


class Consumer(Thread):
    def __init__(self, name):
        super(Consumer, self).__init__()
        self.name = name

    def run(self):
        while True:
            if len(container) > 0:
                product = container.pop()
                print("get product->", product.id)
                time.sleep(1)
            else:
                print("wait for container")


def test():
    p1 = Producer("p1", 1)
    p2 = Producer("p2", 2)
    c1 = Consumer("c1")

    p1.start()
    p2.start()
    c1.start()