import shlex

def detect(process):
    cmd = process["cmd"]

    # 🔥 detect bash reverse shell patterns
    if "/dev/tcp" in cmd or "bash -i" in cmd:
        return f"Reverse shell detected: {cmd}"

    return None

    try:
        args = shlex.split(cmd)
    except:
        return None

    # exact binary match only
    if any(arg in ["nc", "netcat"] for arg in args):
        if "-e" in args or "/bin/sh" in args:
            return f"Reverse shell detected: {cmd}"

    return None