def execute_commands(initial_position, initial_direction, commands):
    position = initial_position
    direction = initial_direction

    for command in commands:
        if command == "f":
            if direction == "N":
                position = (position[0], position[1]+1, position[2])
            elif direction == "S":
                position = (position[0], position[1]-1, position[2])
            elif direction == "E":
                position = (position[0]+1, position[1], position[2])
            elif direction == "W":
                position = (position[0]-1, position[1], position[2])
            elif direction == "Up":
                position = (position[0], position[1], position[2]+1)
            elif direction == "Down":
                position = (position[0], position[1], position[2]-1)

        elif command == "b":
            if direction == "N":
                position = (position[0], position[1]-1, position[2])
            elif direction == "S":
                position = (position[0], position[1]+1, position[2])
            elif direction == "E":
                position = (position[0]-1, position[1], position[2])
            elif direction == "W":
                position = (position[0]+1, position[1], position[2])
            elif direction == "Up":
                position = (position[0], position[1], position[2]-1)
            elif direction == "Down":
                position = (position[0], position[1], position[2]+1)

        elif command == "l":
            if direction == "N":
                direction = "W"
            elif direction == "S":
                direction = "E"
            elif direction == "E":
                direction = "N"
            elif direction == "W":
                direction = "S"

        elif command == "r":
            if direction == "N":
                direction = "E"
            elif direction == "S":
                direction = "W"
            elif direction == "E":
                direction = "S"
            elif direction == "W":
                direction = "N"

        elif command == "u":
            if direction == "N":
                direction = "Up"
            elif direction == "S":
                direction = "Down"
            elif direction == "E":
                direction = "Up"
            elif direction == "W":
                direction = "Down"
            elif direction == "Up":
                pass
            elif direction == "Down":
                pass

        elif command == "d":
            if direction == "N":
                direction = "Down"
            elif direction == "S":
                direction = "Up"
            elif direction == "E":
                direction = "Down"
            elif direction == "W":
                direction = "Up"
            elif direction == "Up":
                pass
            elif direction == "Down":
                pass


    return position, direction