import time
from rich.progress import track

for i in track(range(99), description="For example:"):
    time.sleep(0.05)