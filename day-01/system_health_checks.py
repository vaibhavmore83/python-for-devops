import psutil
def get_cpu_usage():
    user_cpu = int(input("Enter the CPU Threshold: "))
    cpu_usage = psutil.cpu_percent(interval=1)

    if cpu_usage > user_cpu:
        print(f"CPU usage is at {cpu_usage}%, which is above the threshold of {user_cpu}%.")
    else:
        print(f"CPU usage is at {cpu_usage}%, which is within the threshold of {user_cpu}%.")

def get_memory_usage():
    user_memory = int(input("Enter the Memory Threshold: "))
    memory = psutil.virtual_memory()
    memory_usage = memory.percent

    if memory_usage > user_memory:
        print(f"Memory usage is at {memory_usage}%, which is above the threshold of {user_memory}%.")
    else:
        print(f"Memory usage is at {memory_usage}%, which is within the threshold of {user_memory}%.")

def get_disk_usage():
    user_disk = int(input("Enter the Disk Usage Threshold: "))
    disk = psutil.disk_usage('C:')
    disk_usage = disk.percent

    if disk_usage > user_disk:
        print(f"Disk usage is at {disk_usage}%, which is above the threshold of {user_disk}%.")
    else:
        print(f"Disk usage is at {disk_usage}%, which is within the threshold of {user_disk}%.")

print("System Health Checks:")
choice = input("Enter cpu/memory/disk to check respective health checks (enter q to exit): ")

while choice != "q":
    if choice == "cpu":
        get_cpu_usage()
    elif choice == "memory":
        get_memory_usage()
    elif choice == "disk":
        get_disk_usage()
    else:
        print("Invalid choice. Please enter cpu, memory, disk, or q to exit.")
    choice = input("Enter cpu/memory/disk to check respective health checks (enter q to exit): ")