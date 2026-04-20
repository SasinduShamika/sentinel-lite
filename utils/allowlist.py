SAFE_KEYWORDS = [
    "postgres",
    "systemd",
    "sshd",
    ".vscode-server"
]

def is_safe(cmd):
    return any(safe in cmd for safe in SAFE_KEYWORDS)