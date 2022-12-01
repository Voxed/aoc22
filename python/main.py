import importlib
import sys
import os

def run_day(day, ex = False):
    importlib.import_module(f"days.{day}.{day}").start(
        open(
            f"days/{day}/{day}.in" if not ex else f"days/{day}/{day}.ex"
        ).read())

if len(sys.argv) == 1:
    print("Noot enough arguments")
    exit(0)

try:
    day = str(int(sys.argv[1])).rjust(2, '0')
except:
    print("Noot good number")
    exit(0)

if not os.path.exists(f"days/{day}"):
    print("Noot good day")
    exit(0)

run_day(day, len(sys.argv) > 2 and sys.argv[2] == 'ex')