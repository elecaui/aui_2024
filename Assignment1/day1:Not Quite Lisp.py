with open('Floor.txt', 'r') as file_obj:
        input_text = file_obj.read()

instructions =  input_text 

#part 1
def find_floor(instructions):
    current_floor = 0
    for instruction in instructions:
        if instruction == '(':
            current_floor += 1
        elif instruction == ')':
            current_floor -= 1
    return current_floor
 
final_floor = find_floor(instructions)
print("part 1:", final_floor)

#part 2
def find_basement_position(instructions):
    current_floor = 0
    position = 0
    for instruction in instructions:
        position += 1
        if instruction == '(':
            current_floor += 1
        elif instruction == ')':
            current_floor -= 1
        if current_floor == -1:
            return position
    return None

position = find_basement_position(instructions)
if position is not None:
    print("part 2", position)
else:
    print("0")
