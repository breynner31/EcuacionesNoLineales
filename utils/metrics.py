import time
import psutil
import os

def measure_performance(method, *args, **kwargs):
    process = psutil.Process(os.getpid())
    mem_before = process.memory_info().rss / 1024

    start_time = time.time()
    result = method(*args, **kwargs)
    end_time = time.time()

    mem_after = process.memory_info().rss / 1024
    memory_used = mem_after - mem_before

    return {
        "root": result["root"],
        "iterations": result["iterations"],
        "errors": result["errors"],
        "time": end_time - start_time,
        "memory": round(memory_used, 2)
    }
