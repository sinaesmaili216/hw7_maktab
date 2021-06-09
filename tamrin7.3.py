import os 
import argparse

def dir_size(directory):
        total = 0
        for entry in os.scandir(directory):
            if entry.is_file():
                total += entry.stat().st_size
            elif entry.is_dir():
                total += dir_size(entry.path)
        return total 

parser = argparse.ArgumentParser()
parser.add_argument("dir_loc", help="location of a directory")

group = parser.add_mutually_exclusive_group()
group.add_argument("-d", action="store_true")
group.add_argument("-f", action="store_true")

arg = parser.parse_args()

if arg.d:
    print(dir_size(arg.dir_loc))
    
elif arg.f:
    print(os.path.getsize(arg.dir_loc))


