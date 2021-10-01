import random
import sys

# SMALL UNIFORMALLY RANDOM DATASET
def make_data1(f):
    for i in range(200):
        r = random.randint(1, 10)
        f.write(str(r) + "\n")

# LARGER MONOTONAL DATASET
def make_data2(f):
    for i in range(200):
        for j in range(random.randint(1, 10)):
            f.write(str(i) + "\n")

f = open("numbers", "w")

if sys.argv[1] == "1":
    make_data1(f)
elif sys.argv[1] == "2":
    make_data2(f)
else:
    make_data1(f)

f.close()
