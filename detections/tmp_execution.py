def detect(process):
    cmd = process["cmd"]

    # ignore vscode
    if ".vscode-server" in cmd:
        return None

    if "/tmp/" in cmd:
        return f"Execution from /tmp: {cmd}"

    return None