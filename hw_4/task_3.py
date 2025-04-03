import multiprocessing as mp
import threading
import time
import sys
from datetime import datetime
import codecs
import os

def log(msg, prefix="", file=None):
    timestamp = datetime.now().strftime("%H:%M:%S")
    line = f"[{timestamp}] {prefix}{msg}"
    print(line)
    if file:
        file.write(line + "\n")
        file.flush()

def process_a(input_queue, to_b_queue):
    while True:
        msg = input_queue.get()
        if msg == "__exit__":
            break
        processed = msg.lower()
        to_b_queue.put(processed)
        time.sleep(5)

def process_b(from_a_queue, to_main_queue):
    while True:
        msg = from_a_queue.get()
        if msg == "__exit__":
            break
        encoded = codecs.encode(msg, "rot_13")
        print(f"[{datetime.now().strftime('%H:%M:%S')}] B: {encoded}")
        to_main_queue.put(encoded)

def listener(result_queue, log_file):
    while True:
        msg = result_queue.get()
        if msg == "__exit__":
            break
        log(f"Received from B: {msg}", "MAIN: ", file=log_file)

def main():
    os.makedirs("artifacts", exist_ok=True)
    with open("artifacts/task_3.txt", "w") as log_file:
        input_queue = mp.Queue()
        to_b_queue = mp.Queue()
        result_queue = mp.Queue()

        proc_a = mp.Process(target=process_a, args=(input_queue, to_b_queue))
        proc_b = mp.Process(target=process_b, args=(to_b_queue, result_queue))

        proc_a.start()
        proc_b.start()

        listener_thread = threading.Thread(target=listener, args=(result_queue, log_file), daemon=True)
        listener_thread.start()

        try:
            while True:
                user_input = input(">>> ")
                log(f"You entered: {user_input}", "MAIN: ", file=log_file)
                if user_input.lower() in ("exit", "quit"):
                    input_queue.put("__exit__")
                    to_b_queue.put("__exit__")
                    result_queue.put("__exit__")
                    break
                input_queue.put(user_input)
        except KeyboardInterrupt:
            input_queue.put("__exit__")
            to_b_queue.put("__exit__")
            result_queue.put("__exit__")

        proc_a.join()
        proc_b.join()

if __name__ == "__main__":
    mp.set_start_method("fork")
    main()
