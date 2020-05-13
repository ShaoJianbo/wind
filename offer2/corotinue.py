import asyncio
import time


async def fun():
    """异步方法"""
    print("start fun")
    ans = 0
    # 等待1s的IO完成
    await asyncio.sleep(1)
    for i in range(1000):
        ans += i
    print("end fun")
    print(f"ans->{ans}")


async def foo2():
    print('----start foo')
    # time.sleep(1)
    await asyncio.sleep(1)
    print('----end foo')


async def bar2():
    print('----start bar')
    # time.sleep(2)
    await asyncio.sleep(2)
    print('----end bar')


async def test():
    res = await asyncio.gather(bar2(), foo2())
    # print(res)

if __name__ == '__main__':
    start_time = time.time()
    asyncio.run(test())
    end_time = time.time()
    print(f"run {end_time-start_time} seconds")

# if __name__ == '__main__':
#     asyncio.run(fun())
