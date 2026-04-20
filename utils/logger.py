import datetime

def log(message):
    timestamp = datetime.datetime.now()
    print(f"[{timestamp}] {message}")