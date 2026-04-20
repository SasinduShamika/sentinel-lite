import time
from process_collector import get_processes
from utils.logger import log

# import detection modules
import detections.reverse_shell as reverse_shell
import detections.tmp_execution as tmp_execution

DETECTIONS = [
    reverse_shell,
    tmp_execution
]

seen = set()

def run_detection(process):
    for module in DETECTIONS:
        result = module.detect(process)
        if result and process["pid"] not in seen:
            log(result)
            seen.add(process["pid"])

while True:
    processes = get_processes()

    for process in processes:
        run_detection(process)

    time.sleep(2)