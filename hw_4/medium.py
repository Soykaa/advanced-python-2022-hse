import concurrent
import math
import time
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor

import multiprocessing as mp


def integrate(f, a, b, job_n, n_jobs=1, n_iter=1000):
    acc = 0
    step = (b - a) / n_iter
    left_b, right_b = n_iter // n_jobs * job_n, min(n_iter, n_iter // n_jobs * (job_n + 1))
    for i in range(left_b, right_b):
        acc += f(a + i * step) * step
    return acc


def execute_pool_tasks(executor, n_jobs):
    futures = []
    res = 0
    fst_timestamp = time.time()
    for job_n in range(n_jobs):
        futures.append(executor.submit(integrate, f=math.cos, a=0, b=math.pi / 2, job_n=job_n, n_jobs=n_jobs))
    for future in concurrent.futures.as_completed(futures):
        res += future.result()
    snd_timestamp = time.time()
    return fst_timestamp, snd_timestamp, res


if __name__ == '__main__':
    with open("artifacts/medium.txt", "w") as file:
        cpu_num = mp.cpu_count()
        for n_jobs in range(1, 2 * cpu_num + 1):
            thread_pool_executor = ThreadPoolExecutor(max_workers=10)
            start, end, res = execute_pool_tasks(thread_pool_executor, n_jobs)
            file.write(f'{n_jobs} threads...\n\t'
                       f'Res: {res}\n\t'
                       f'Time: {end - start} sec\n')

            process_pool_executor = ProcessPoolExecutor(max_workers=10)
            start, end, res = execute_pool_tasks(process_pool_executor, n_jobs)
            file.write(f'{n_jobs} processes...\n\t'
                       f'Res: {res}\n\t'
                       f'Time: {end - start} sec\n\n')
