def return_wire_step_count(wire, intersection_direction, last_step):
    count = 0
    wire_to_intersection = wire[:wire.index(intersection_direction) + 1]
    for direction in wire_to_intersection:
        if direction == wire_to_intersection[-1]:
            print(last_step)
            count += last_step
        else:
            print(direction)
            count += int(direction[1:])
    print()
    return count

with open("input", "r") as f:
    input_file = f.readlines()
    wire1 = [x.strip() for x in input_file[0].split(",")]
    wire2 = [y.strip() for y in input_file[1].split(",")]

    # x, y
    wire1_coordinates = [[0, 0]]
    wire2_coordinates = [[0, 0]]

    wire1_positions = set()
    wire1_positions_directions = list()

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
            for i, x in enumerate(range(next_to_last_x + 1, last_x + 1)):
                wire1_positions.add((x, last_y))
                wire1_positions_directions.append(((x, last_y), direction, i + 1))

        elif wire1_direction[0] == "L":
            last_x = wire1_coordinates[-1][0] - wire1_direction[1]
            last_y = wire1_coordinates[-1][1]

            wire1_coordinates.append((last_x, last_y))

            next_to_last_x = wire1_coordinates[-2][0]
            next_to_last_y = wire1_coordinates[-2][0]

            # Get each x coordinate where the wire went (y remains unchanged)
            for i, x in enumerate(reversed(range(last_x, next_to_last_x))):
                wire1_positions.add((x, last_y))
                wire1_positions_directions.append(((x, last_y), direction, i + 1))

        elif wire1_direction[0] == "U":
            last_x = wire1_coordinates[-1][0]
            last_y = wire1_coordinates[-1][1] + wire1_direction[1]

            wire1_coordinates.append((last_x, last_y))

            next_to_last_x = wire1_coordinates[-2][0]
            next_to_last_y = wire1_coordinates[-2][1]

            for i, y in enumerate(range(next_to_last_y + 1, last_y + 1)):
                wire1_positions.add((last_x, y))
                wire1_positions_directions.append(((last_x, y), direction, i + 1))

        else:
            last_x = wire1_coordinates[-1][0]
            last_y = wire1_coordinates[-1][1] - wire1_direction[1]

            wire1_coordinates.append((last_x, last_y))

            next_to_last_x = wire1_coordinates[-2][0]
            next_to_last_y = wire1_coordinates[-2][1]
            for i, y in enumerate(reversed(range(last_y, next_to_last_y))):
                wire1_positions.add((last_x, y))
                wire1_positions_directions.append(((last_x, y), direction, i + 1))
    
    for direction in wire2:
        wire2_direction = (direction[0], int(direction[1:]))
        if wire2_direction[0] == "R":
            last_x = wire2_coordinates[-1][0] + wire2_direction[1]
            last_y = wire2_coordinates[-1][1]

            wire2_coordinates.append((last_x, last_y))

            next_to_last_x = wire2_coordinates[-2][0]
            next_to_last_y = wire2_coordinates[-2][0]

            # Get each x coordinate where the wire went (y remains unchanged)
            for i, x in enumerate(range(next_to_last_x + 1, last_x + 1)):
                if (x, last_y) in wire1_positions:
                    wire1_intersection_direction = None
                    wire1_last_step = 0
                    for position_direction in wire1_positions_directions:
                        if position_direction[0] == (x, last_y):
                            wire1_intersection_direction = position_direction[1]
                            wire1_last_step = position_direction[2]

                    wire1_step_count = return_wire_step_count(wire1, wire1_intersection_direction, wire1_last_step)
                    wire2_step_count = return_wire_step_count(wire2, direction, i + 1)

                    intersections.append([(x, last_y), wire1_step_count + wire2_step_count])

        elif wire2_direction[0] == "L":
            last_x = wire2_coordinates[-1][0] - wire2_direction[1]
            last_y = wire2_coordinates[-1][1]

            wire2_coordinates.append((last_x, last_y))

            next_to_last_x = wire2_coordinates[-2][0]
            next_to_last_y = wire2_coordinates[-2][0]

            # Get each x coordinate where the wire went (y remains unchanged)
            for i, x in enumerate(reversed(range(last_x, next_to_last_x))):
                if (x, last_y) in wire1_positions:
                    for position_direction in wire1_positions_directions:
                        if position_direction[0] == (x, last_y):
                            wire1_intersection_direction = position_direction[1]
                            wire1_last_step = position_direction[2]

                    wire1_step_count = return_wire_step_count(wire1, wire1_intersection_direction, wire1_last_step)
                    wire2_step_count = return_wire_step_count(wire2, direction, i + 1)

                    intersections.append([(x, last_y), wire1_step_count + wire2_step_count])

        elif wire2_direction[0] == "U":
            last_x = wire2_coordinates[-1][0]
            last_y = wire2_coordinates[-1][1] + wire2_direction[1]

            wire2_coordinates.append((last_x, last_y))

            next_to_last_x = wire2_coordinates[-2][0]
            next_to_last_y = wire2_coordinates[-2][1]

            for i, y in enumerate(range(next_to_last_y, last_y + 1)):
                if (last_x, y) in wire1_positions:
                    for position_direction in wire1_positions_directions:
                        if position_direction[0] == (last_x, y):
                            wire1_intersection_direction = position_direction[1]
                            wire1_last_step = position_direction[2]

                    wire1_step_count = return_wire_step_count(wire1, wire1_intersection_direction, wire1_last_step)
                    wire2_step_count = return_wire_step_count(wire2, direction, i + 1)

                    intersections.append([(last_x, y), wire1_step_count + wire2_step_count])
        else:
            last_x = wire2_coordinates[-1][0]
            last_y = wire2_coordinates[-1][1] - wire2_direction[1]

            wire2_coordinates.append((last_x, last_y))

            next_to_last_x = wire2_coordinates[-2][0]
            next_to_last_y = wire2_coordinates[-2][1]
            for i, y in enumerate(reversed(range(last_y, next_to_last_y))):
                if (last_x, y) in wire1_positions:
                    for position_direction in wire1_positions_directions:
                        if position_direction[0] == (last_x, y):
                            wire1_intersection_direction = position_direction[1]
                            wire1_last_step = position_direction[2]

                    wire1_step_count = return_wire_step_count(wire1, wire1_intersection_direction, wire1_last_step)
                    wire2_step_count = return_wire_step_count(wire2, direction, i + 1)

                    intersections.append([(last_x, y), wire1_step_count + wire2_step_count])

    print(intersections)
    print("Fewest combined steps the wires must take to reach an intersection:", min([x[1] for x in intersections]))
        
