from spacecraft import execute_commands

initial_position = (0, 0, 0)
initial_direction = "N"
commands = ["l", "f"]

final_position, final_direction = execute_commands(initial_position, initial_direction, commands)

print(final_position)
print(final_direction)