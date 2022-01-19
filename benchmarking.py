import time
import math
import random

time_list = []
triggers = ["processing", "updating", "creating", "resolving", "downloading"]
count = 0

time.sleep(1)

def delta_time(arg):
    if arg >= 60:
        a = math.floor(arg/60)
        b = round(arg%60, 2)
        tim_a = f"{a} Minutes {b} Seconds"
    elif arg >=3600:
        a = math.floor(arg/3600)
        b = math.floor(arg%3600/60)
        c = round(arg%60, 2)
        tim_a = f"{a} Hours {b} Minutes {c} Seconds"
    elif arg < 60:
        tim_a = f"{round(arg, 2)} Seconds"
    return tim_a

def busywork():
    global count
    start_time = time.perf_counter()
    try:
        with open("/Users/aaatipamula/Documents/vscode_projects/busywork/usernames.txt", "r") as f:
            user = f.readlines()
            with open("/Users/aaatipamula/Documents/vscode_projects/busywork/files.txt", "r") as f:
                files = f.readlines()
                for x in user:
                    x_a = x.replace('\n', '')
                    for y in files:
                        y_a = y.replace('\n', '')
                        count += 1
                        print(f"{random.choice(triggers)} {y_a} for {x_a}...")

        tim = round(time.perf_counter()-start_time, 2)
        time.sleep(1)
        print(f"\nYou finished the program!\n{count:,} lines were printed out!\nIt took {delta_time(tim)} seconds!\n")
    except KeyboardInterrupt:
        tim = round(time.perf_counter()-start_time, 2)
        print(f"\nYou stopped the program.\n{count:,} lines were printed out!\nIt took {delta_time(tim)} seconds!\n")

busywork()