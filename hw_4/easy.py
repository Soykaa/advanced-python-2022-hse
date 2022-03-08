import concurrent
import time
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor

NUMBER = 30000
ITERATIONS = 10


def fib_numbers(n):
    res = [1, 1]
    fib_num1 = fib_num2 = 1
    for i in range(2, n):
        fib_num3 = fib_num1 + fib_num2
        fib_num1 = fib_num2
        fib_num2 = fib_num3
        res.append(fib_num2)
    return res


def execute_sync_task():
    fst_timestamp = time.time()
    for _ in range(ITERATIONS):
        fib_numbers(NUMBER)
    snd_timestamp = time.time()
    return fst_timestamp, snd_timestamp


def execute_pool_tasks(executor):
    futures = []
    fst_timestamp = time.time()
    for _ in range(ITERATIONS):
        futures.append(executor.submit(fib_numbers, NUMBER))
    for future in concurrent.futures.as_completed(futures):
        future.result()
    snd_timestamp = time.time()
    return fst_timestamp, snd_timestamp


if __name__ == '__main__':
    with open("artifacts/easy.txt", "w") as file:
        start, end = execute_sync_task()
        file.write("Synchronous: " + str(end - start) + " sec\n\n")
        thread_pool_executor = ThreadPoolExecutor(max_workers=10)
        start, end = execute_pool_tasks(thread_pool_executor)
        file.write("Threading: " + str(end - start) + " sec\n\n")
        process_pool_executor = ProcessPoolExecutor(max_workers=10)
        start, end = execute_pool_tasks(process_pool_executor)
        file.write("Multiprocessing: " + str(end - start) + " sec\n\n")
