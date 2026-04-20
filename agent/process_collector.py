import os

def get_processes():
    processes = {}

    for pid in os.listdir('/proc'):
        if pid.isdigit():
            try:
                with open(f'/proc/{pid}/cmdline', 'r') as f:
                    cmd = f.read().replace('\x00', ' ').strip()

                if not cmd:
                    continue

                with open(f'/proc/{pid}/stat', 'r') as f:
                    stat = f.read().split()
                    ppid = stat[3]
                    name = stat[1].strip("()")

                processes[pid] = {
                    "pid": pid,
                    "ppid": ppid,
                    "cmd": cmd,
                    "name": name
                }
            except:
                continue

    return processes