import psutil
import time

def get_resource_usage():
    print("Fetching system resource usage...\n")
    print(f"CPU Usage: {psutil.cpu_percent()}%")
    print(f"Memory Usage: {psutil.virtual_memory().percent}%")
    print(f"Disk Usage: {psutil.disk_usage('/').percent}%\n")

if _name_ == "_main_":
    while True:
        get_resource_usage()
        time.sleep(5)