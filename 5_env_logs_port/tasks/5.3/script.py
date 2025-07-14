import sys
from time import sleep

print("Generating logs")

for i in range(1, 6):
    print(f"LOG - {i}")
    print(f"ERROR - {i}", file=sys.stderr)
    sleep(1)

print("Done")