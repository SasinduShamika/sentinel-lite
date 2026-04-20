import os

def get_processes():
    processes = []
    for pid in os.listdir('/proc'):
        if pid.isdigit():
            try:
                with open(f'/proc/{pid}/cmdline', 'r') as f:
                    cmd = f.read().replace('\x00', ' ').strip()

                if not cmd:
                    continue

                with open(f'/proc/{pid}/stat', 'r') as f:
                    ppid = f.read().split()[3]

                processes.append({
                    "pid": pid,
                    "ppid": ppid,
                    "cmd": cmd
                })
            except:
                continue
    return processes