import time
import random
import math
import concurrent.futures

triggers = ["processing", "updating", "creating", "resolving", "downloading"]
count = 0


def speed():
    arg2 = input("Slow or way to fast to stop? [s/f]: ")
    if arg2 == "s" or arg2 == "slow":
        busywork(0.1)
    elif arg2 == "f" or arg2 == "fast":
        busywork(0)
    else:
        print("\nPlease enter a valid argument.\n")
        speed()

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

def busywork(arg):
    start_time = time.perf_counter()

    try:
        users_list = []
        with open("/Users/aaatipamula/Documents/local_projects/usernames.txt", "r") as f:
            user = f.readlines()
            for x in user:
                x_a = x.replace('\n', '')
            with open("/Users/aaatipamula/Documents/local_projects/files_cp.txt", "r") as f:
                files = f.readlines()
                for y in files:
                    y_a = y.replace('\n', '')
                    count += 1
                    print(f"{random.choice(triggers)} {y_a} for {x_a}...")
                    time.sleep(random.uniform(0,arg))
                    

        tim = round(time.perf_counter()-start_time, 2)
        print(f"\nYou finished printing out all the combinations!\n{count:,} lines were printed!\nIt took {delta_time(tim)}\n")
    except KeyboardInterrupt:
        tim = time.perf_counter()-start_time
        print(f"\nYou stopped the command.\n{count:,} lines were printed!\nIt took {delta_time(tim)}\n")
        start()

if __name__ == "__main__":
    speed()