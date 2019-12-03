import sys
from itertools import product
def compile_intcode(intcode, noun, verb):
    i = 0
    intcode[1] = noun
    intcode[2] = verb
    while intcode[i] != 99:
        input1_pos = intcode[i + 1]
        input2_pos = intcode[i + 2]
        output1_pos = intcode[i + 3]
        if intcode[i] == 1: intcode[output1_pos] = intcode[input1_pos] + intcode[input2_pos]
        if intcode[i] == 2: intcode[output1_pos] = intcode[input1_pos] * intcode[input2_pos]
        i += 4
    return intcode[0]

with open("input", "r") as f:
    intcode = list(map(int, [x.strip() for x in f.readlines()][0].split(",")))
    intcode_copy = intcode[:]
    for i, j in product(list(range(0, 99)), repeat=2):
        if compile_intcode(intcode_copy, i, j) == 19690720:
            print("Pair found")
            print("noun:", i)
            print("verb:", j)
            sys.exit()
        intcode_copy = intcode[:]


