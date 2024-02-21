
with open('day3.txt', 'r') as file_obj:
    input_text = file_obj.read()


# part 1:
# Starting point
# north (^), south (v), east (>), or west (<)

instructions = input_text

def twice_location(instructions):
    visied_locations = {(0, 0)}
    starting_location = [0,0]
    for instructions in instructions:
        if instructions == '>':
            starting_location[0] += 1 
        elif instructions == '<':
            starting_location[0] -= 1
        elif instructions == '^':
            starting_location[1] += 1
        elif instructions == 'v':
            starting_location[1] -= 1
        visied_locations.add(tuple(starting_location))  # Add current position to visited houses
    return len(visied_locations)

print("# at least one present:", twice_location(instructions))

# part 2:
# Robo-Santa

def robosanta(instructions):
    visied_locations = {(0, 0)}
    santa_location = [0,0]
    robosanta_location = [0,0]
    santa_move = True

    for instructions in instructions:
        if santa_move == True:
            current_locations = santa_location
        else:
            current_locations = robosanta_location
        
        if instructions == '>':
            current_locations[0] += 1 
        elif instructions == '<':
            current_locations[0] -= 1
        elif instructions == '^':
            current_locations[1] += 1
        elif instructions == 'v':
            current_locations[1] -= 1

        visied_locations.add(tuple(current_locations))
        santa_move = not santa_move
        
    return len(visied_locations)

print("part 2:", robosanta(instructions))

