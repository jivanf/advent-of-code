with open("input_test2", "r") as f:
    input_file = f.readlines()
    wire1 = [x.strip() for x in input_file[0].split(",")]
    wire2 = [y.strip() for y in input_file[1].split(",")]

    # x, y
    wire1_coordinates = [[0, 0]]
    wire2_coordinates = [[0, 0]]

    wire1_positions = set()

    intersections = list()

    for direction in wire1:
        wire1_direction = (direction[0], int(direction[1:]))
        if wire1_direction[0] == "R":
            last_x = wire1_coordinates[-1][0] + wire1_direction[1]
            last_y = wire1_coordinates[-1][1]

            wire1_coordinates.append((last_x, last_y))

            next_to_last_x = wire1_coordinates[-2][0]
            next_to_last_y = wire1_coordinates[-2][0]

            # Get each x coordinate where the wire went (y remains unchanged)
            for x in range(next_to_last_x + 1, last_x + 1):
                wire1_positions.add((x, last_y))

        elif wire1_direction[0] == "L":
            last_x = wire1_coordinates[-1][0] - wire1_direction[1]
            last_y = wire1_coordinates[-1][1]

            wire1_coordinates.append((last_x, last_y))

            next_to_last_x = wire1_coordinates[-2][0]
            next_to_last_y = wire1_coordinates[-2][0]

            # Get each x coordinate where the wire went (y remains unchanged)
            for x in reversed(range(last_x, next_to_last_x)):
                wire1_positions.add((x, last_y))

        elif wire1_direction[0] == "U":
            last_x = wire1_coordinates[-1][0]
            last_y = wire1_coordinates[-1][1] + wire1_direction[1]

            wire1_coordinates.append((last_x, last_y))

            next_to_last_x = wire1_coordinates[-2][0]
            next_to_last_y = wire1_coordinates[-2][1]

            for y in range(next_to_last_y + 1, last_y + 1):
                wire1_positions.add((last_x, y))

        else:
            last_x = wire1_coordinates[-1][0]
            last_y = wire1_coordinates[-1][1] - wire1_direction[1]

            wire1_coordinates.append((last_x, last_y))

            next_to_last_x = wire1_coordinates[-2][0]
            next_to_last_y = wire1_coordinates[-2][1]
            for y in reversed(range(last_y, next_to_last_y)):
                wire1_positions.add((last_x, y))
    
    for direction in wire2:
        wire2_direction = (direction[0], int(direction[1:]))
        if wire2_direction[0] == "R":
            last_x = wire2_coordinates[-1][0] + wire2_direction[1]
            last_y = wire2_coordinates[-1][1]

            wire2_coordinates.append((last_x, last_y))

            next_to_last_x = wire2_coordinates[-2][0]
            next_to_last_y = wire2_coordinates[-2][0]

            # Get each x coordinate where the wire went (y remains unchanged)
            for x in range(next_to_last_x + 1, last_x + 1):
                if (x, last_y) in wire1_positions:
                    print((x, last_y), wire2_direction[0])
                    intersections.append((x, last_y))

        elif wire2_direction[0] == "L":
            last_x = wire2_coordinates[-1][0] - wire2_direction[1]
            last_y = wire2_coordinates[-1][1]

            wire2_coordinates.append((last_x, last_y))

            next_to_last_x = wire2_coordinates[-2][0]
            next_to_last_y = wire2_coordinates[-2][0]

            # Get each x coordinate where the wire went (y remains unchanged)
            for x in reversed(range(last_x, next_to_last_x)):
                if (x, last_y) in wire1_positions:
                    print((x, last_y), wire2_direction[0])
                    intersections.append((x, last_y))

        elif wire2_direction[0] == "U":
            last_x = wire2_coordinates[-1][0]
            last_y = wire2_coordinates[-1][1] + wire2_direction[1]

            wire2_coordinates.append((last_x, last_y))

            next_to_last_x = wire2_coordinates[-2][0]
            next_to_last_y = wire2_coordinates[-2][1]

            for y in range(next_to_last_y, last_y + 1):
                if (last_x, y) in wire1_positions:
                    print((last_x, y), wire2_direction[0])
                    intersections.append((last_x, y))

        else:
            last_x = wire2_coordinates[-1][0]
            last_y = wire2_coordinates[-1][1] - wire2_direction[1]

            wire2_coordinates.append((last_x, last_y))

            next_to_last_x = wire2_coordinates[-2][0]
            next_to_last_y = wire2_coordinates[-2][1]
            for y in reversed(range(last_y, next_to_last_y)):
                if (last_x, y) in wire1_positions:
                    print((last_x, y), wire2_direction[0])
                    intersections.append((last_x, y))
    print(intersections)
    print("Manhattan distance from the closest intersection to the central port:", min([sum(list(map(abs, x))) for x in intersections]))
        
