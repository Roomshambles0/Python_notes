import psutil
processes = psutil.process_iter()
for process in processes:
    print(f"Process name: {process.name()} | PID: {process.pid}")
cpu_percent = psutil.cpu_percent()
print(f"CPU usage: {cpu_percent}%")
memory_usage = psutil.virtual_memory()
print(f"Total memory: {memory_usage.total / 1024 / 1024:.2f} MB")
print(f"Available memory: {memory_usage.available / 1024 / 1024:.2f} MB")
print(f"Memory usage: {memory_usage.percent}%")