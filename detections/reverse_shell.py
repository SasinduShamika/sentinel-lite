def detect(process):
    cmd = process["cmd"]

    indicators = ['nc', 'bash -i', '/dev/tcp']

    if any(x in cmd for x in indicators):
        return f"Reverse shell detected: {cmd}"

    return None