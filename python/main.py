import importlib
import sys
import os

def run_day(day, ex = False, imp = False):
    i = "_improved" if imp else ""
    folder = f"days/{day}{i}"
    if not os.path.exists(folder):
        print("Noot good day")
        return
    importlib.import_module(f"days.{day}{i}.{day}").start(
        open(
            f"{folder}/{day}.in" if not ex else f"{folder}/{day}.ex"
        ).read())

if len(sys.argv) == 1:
    print("Noot enough arguments")
    exit(0)

try:
    day = str(int(sys.argv[1])).rjust(2, '0')
except:
    print("Noot good number")
    exit(0)


run_day(day, len(sys.argv) > 2 and 'ex' in sys.argv[2:], len(sys.argv) > 2 and 'improved' in sys.argv[2:])