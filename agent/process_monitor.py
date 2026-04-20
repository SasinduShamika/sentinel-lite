import os
import time


def get_processes():
    processes = []
    for pid in os.listdir('/proc'):
        if pid.isdigit():
            try:
                with open(f'/proc/{pid}/cmdline', 'r') as f:
                    cmd = f.read().replace('\x00', ' ').strip()
                with open(f'/proc/{pid}/stat', 'r') as f:
                    ppid = f.read().split()[3]
                processes.append((pid, ppid, cmd))
            except:
                continue
    return processes

def detect_suspicious(processes):
    for pid, ppid, cmd in processes:
        if 'nc' in cmd or 'bash -i' in cmd:
            print(f"[ALERT] Suspicious process: PID={pid}, CMD={cmd}")

while True:
    procs = get_processes()
    detect_suspicious(procs)
    time.sleep(2)