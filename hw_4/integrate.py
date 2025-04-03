import time
import math
import os
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
from multiprocessing import cpu_count

def integrate_chunk(f, a, b, n_iter):
    acc = 0
    step = (b - a) / n_iter
    for i in range(n_iter):
        acc += f(a + i * step) * step
    return acc

def integrate(f, a, b, *, n_jobs=1, n_iter=10_000_000, executor_type="thread"):
    chunk_size = n_iter // n_jobs
    chunk_bounds = [
        (a + i * (b - a) / n_jobs, a + (i + 1) * (b - a) / n_jobs)
        for i in range(n_jobs)
    ]

    Executor = ThreadPoolExecutor if executor_type == "thread" else ProcessPoolExecutor

    with Executor(max_workers=n_jobs) as executor:
        futures = [executor.submit(integrate_chunk, f, x0, x1, chunk_size)
                   for (x0, x1) in chunk_bounds]
        results = [f.result() for f in futures]

    return sum(results)

def benchmark():
    max_jobs = cpu_count() * 2
    results = []

    for n_jobs in range(1, max_jobs + 1):
        # Threading
        start = time.time()
        integrate(math.cos, 0, math.pi / 2, n_jobs=n_jobs, executor_type="thread")
        thread_time = time.time() - start

        # Processing
        start = time.time()
        integrate(math.cos, 0, math.pi / 2, n_jobs=n_jobs, executor_type="process")
        process_time = time.time() - start

        results.append((n_jobs, thread_time, process_time))

    return results

def write_results(results, filename="artifacts/task_2.txt"):
    os.makedirs("artifacts", exist_ok=True)
    with open(filename, "w") as f:
        f.write("n_jobs\tThread\tProcess\n")
        for n_jobs, thread_time, process_time in results:
            f.write(f"{n_jobs}\t{thread_time:.4f}\t\t{process_time:.4f}\n")

if __name__ == "__main__":
    data = benchmark()
    write_results(data)
    print("Results saved to artifacts/task_2.txt")
