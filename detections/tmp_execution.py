def detect(process):
    cmd = process["cmd"]

    if '/tmp/' in cmd:
        return f"Execution from /tmp: {cmd}"

    return None