import time

from agent.process_collector import get_processes
from utils.logger import log
from utils.allowlist import is_safe

# import detection modules
import detections.reverse_shell as reverse_shell
import detections.tmp_execution as tmp_execution

DETECTIONS = [
    reverse_shell,
    tmp_execution
]

seen = set()

def run_detection(process):
    cmd = process["cmd"]

    # 🔥 Skip safe processes
    if is_safe(cmd):
        return

    for module in DETECTIONS:
        try:
            result = module.detect(process)
        except Exception as e:
            # prevent one broken detection from crashing everything
            log(f"[ERROR] {module.__name__}: {e}")
            continue

        if result and process["pid"] not in seen:
            log(result)
            seen.add(process["pid"])

def main():
    log("Sentinel Lite started...")

    while True:
        processes = get_processes()

        for process in processes:
            run_detection(process)

        time.sleep(2)

if __name__ == "__main__":
    main()