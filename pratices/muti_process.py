from random import randint
from time import time, sleep
import os
from multiprocessing import process
from threading import Thread


def task(filename):
    pid = os.getpid()
    thread = os.getpgid(pid)
    print(f"pid {pid} start to open {filename} {thread}")
    sleep_time = 2
    sleep(sleep_time)
    print(f"end to open {filename}")


def run_task():
    start = time()
    # task("python.pdf")
    # task("c++.pdf")
    from multiprocessing import Process
    task1 = Process(target=task, args=("python.pdf", ))
    task1 = Thread(target=task, args=("python.pdf",))
    task1.start()
    task2 = Process(target=task, args=("C++.pdf", ))
    task2 = Thread(target=task, args=("C++.pdf",))
    task2.start()
    task1.join()
    task2.join()
    end = time()
    task_time = end - start
    print(f"This task run {task_time}")


if __name__ == "__main__":
    run_task()
