import os
import sys


path = "/Users/rohan/dev/Python"

def create():
    fileName = str(sys.argv[1])

    loc = os.path.join(path, fileName)

    os.makedirs(loc)


if __name__ == "__main__":
    create()
