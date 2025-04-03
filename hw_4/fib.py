import os
import time
import threading
import multiprocessing

def fib(n):
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)

N = 30
REPEATS = 10

def run_sync():
    start = time.time()
    for _ in range(REPEATS):
        fib(N)
    return time.time() - start

def run_threads():
    threads = []
    start = time.time()
    for _ in range(REPEATS):
        t = threading.Thread(target=fib, args=(N,))
        t.start()
        threads.append(t)
    for t in threads:
        t.join()
    return time.time() - start

def run_processes():
    processes = []
    start = time.time()
    for _ in range(REPEATS):
        p = multiprocessing.Process(target=fib, args=(N,))
        p.start()
        processes.append(p)
    for p in processes:
        p.join()
    return time.time() - start

if __name__ == "__main__":
    sync_time = run_sync()
    thread_time = run_threads()
    process_time = run_processes()

    # Убедимся, что папка artifacts существует
    os.makedirs("artifacts", exist_ok=True)

    with open("artifacts/task_1.txt", "w") as f:
        f.write(f"Fibonacci benchmark for N={N}, repeats={REPEATS}\n")
        f.write(f"Synchronous:     {sync_time:.2f} seconds\n")
        f.write(f"Threading:       {thread_time:.2f} seconds\n")
        f.write(f"Multiprocessing: {process_time:.2f} seconds\n")

    print("Results saved to artifacts/task_1.txt")
