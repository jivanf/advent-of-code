with open("input", "r") as f:
    intcode = list(map(int, [x.strip() for x in f.readlines()][0].split(",")))
    intcode[1] = 12
    intcode[2] = 2
    i = 0
    while intcode[i] != 99:
        input1_pos = intcode[i + 1]
        input2_pos = intcode[i + 2]
        output1_pos = intcode[i + 3]
        print("output1:", intcode[output1_pos])
        print("input1:", intcode[input1_pos])
        print("input2:", intcode[input2_pos])
        if intcode[i] == 1: intcode[output1_pos] = intcode[input1_pos] + intcode[input2_pos]
        if intcode[i] == 2: intcode[output1_pos] = intcode[input1_pos] * intcode[input2_pos]
        i += 4
    print(intcode)
            
            
