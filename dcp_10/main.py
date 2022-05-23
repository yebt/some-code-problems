import asyncio
import time

async def job(func, sleep_time):
    milliseconds = sleep_time/1000
    await asyncio.sleep(milliseconds)
    func()

async def main():
    task_1  = asyncio.create_task(job(lambda : print("this is the task"), 2000))
    await task_1

if __name__ == '__main__':
    asyncio.run(main())
