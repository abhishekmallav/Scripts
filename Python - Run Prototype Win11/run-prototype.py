import psutil

def set_cpu_affinity(exe_path, cpu_limit):
    process = psutil.Popen(exe_path)
    pid = process.pid
    affinity = list(range(cpu_limit))
    psutil.Process(pid).cpu_affinity(affinity)
    print(f"Started {exe_path} with CPU cores {affinity}")


if __name__ == "__main__":
    # TODO: Replace with the local path to the executable.
    exe_path = r"<EXECUTABLE_PATH>"
    cpu_limit = 2                                     # use CPU 0 and 1
    set_cpu_affinity(exe_path, cpu_limit)
