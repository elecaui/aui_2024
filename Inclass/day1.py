# Direction Map : Facing North, Start at (0, 0)

direction_map = {
    'N': {'L': 'W', 'R': 'E'},
    'E': {'L': 'N', 'R': 'S'},
    'S': {'L': 'E', 'R': 'W'},
    'W': {'L': 'S', 'R': 'N'},
}

# Starting point
position_x, position_y = 0, 0
current_direction = 'N'

# Input
with open('day1.txt', 'r') as file_obj:
    input_text = file_obj.read()
for instruction in input_text.split(', '):
    left_right = instruction[0]
    step_text = instruction[1:]
    steps = int(step_text)

    new_direction = direction_map[current_direction][left_right]
    if new_direction == 'N': 
        position_y = position_y + steps  # Go north
    elif new_direction == 'S':
        position_y = position_y - steps  # Go sourth
    elif new_direction == 'E':
        position_x = position_x + steps  # Go east
    elif new_direction == 'W':
        position_x = position_x - steps    # Go west

    current_direction = new_direction

# Print result
print(f'Ending position: ({position_x},{position_y})')
print(f'Distance: {abs(position_x) + abs(position_y)}')