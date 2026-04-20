def detect(process, processes):
    pid = process["pid"]
    ppid = process["ppid"]

    parent = processes.get(ppid)
    if not parent:
        return None

    parent_cmd = parent["cmd"]
    cmd = process["cmd"]

    # ✅ normal shells from ssh (ignore)
    if "sshd" in parent_cmd and ("bash" in cmd or "sh" in cmd):
        return None

    # 🔥 suspicious: ssh spawning something unusual
    if "sshd" in parent_cmd and not any(x in cmd for x in ["bash", "sh"]):
        return f"Suspicious process from SSH: {parent_cmd} → {cmd}"

    return None