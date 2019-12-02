import math

with open("input", "r") as f:
    print(sum([math.floor(int(x) / 3) - 2 for x in [x.strip() for x in f.readlines()]]))
