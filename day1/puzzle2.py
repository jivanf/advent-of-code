import math

def calculate_fuel(fuel):
    current_fuel = math.floor(int(fuel / 3)) - 2
    if current_fuel < 1:
        return fuel
    else:
        return fuel + calculate_fuel(current_fuel)

with open("input", "r") as f:
    print(sum([calculate_fuel(math.floor(int(x) / 3) - 2) for x in [y.strip() for y in f.readlines()]]))
