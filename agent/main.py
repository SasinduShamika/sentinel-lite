import time
import detections.process_tree as process_tree
from agent.process_collector import get_processes
from utils.logger import log
from utils.allowlist import is_safe

# import detection modules
import detections.reverse_shell as reverse_shell
import detections.tmp_execution as tmp_execution

DETECTIONS = [
    reverse_shell,
    tmp_execution,
    process_tree
]

seen = set()

def run_detection(process, processes):
    cmd = process["cmd"]

    # skip safe processes
    if is_safe(cmd):
        return

    for module in DETECTIONS:
        try:
            # 🔥 support both types of detection functions
            try:
                result = module.detect(process, processes)
            except TypeError:
                result = module.detect(process)

        except Exception as e:
            log(f"[ERROR] {module.__name__}: {e}")
            continue

        if result and process["pid"] not in seen:
            log(result)
            seen.add(process["pid"])

def main():
    log("Sentinel Lite started...")

    while True:
        processes = get_processes()

        for process in processes.values():
            run_detection(process, processes)

            time.sleep(0.5)

if __name__ == "__main__":
    main()