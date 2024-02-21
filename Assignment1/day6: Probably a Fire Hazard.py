import pandas as pd

with open('day6.txt', 'r') as file_obj:
    instructions = file_obj.readlines()

# part1
    
grid = pd.DataFrame(0, index=range(1000), columns=range(1000))

def light_instruction(instruction):
    words = instruction.replace(',', ' ').split()
    if words[0] == 'toggle':
        x1, y1 = int(words[1]), int(words[2])
        x2, y2 = int(words[4]), int(words[5])
    else:
        x1, y1 = int(words[2]), int(words[3])
        x2, y2 = int(words[5]), int(words[6])

    if words[1] == 'on':
        grid.loc[x1:x2, y1:y2] = 1
    elif words[1] == 'off':
        grid.loc[x1:x2, y1:y2] = 0
    elif words[0] == 'toggle':
        grid.loc[x1:x2, y1:y2] = 1 - grid.loc[x1:x2, y1:y2]

for instruction in instructions:
    light_instruction(instruction)

num_lights_lit = grid.values.sum()
print("part1 # of lights lit:", num_lights_lit)


#part 2
grid = pd.DataFrame(0, index=range(1000), columns=range(1000))

def brightness(instructions):
    words = instruction.replace(',', ' ').split()
    if words[0] == 'toggle':
        x1, y1 = int(words[1]), int(words[2])
        x2, y2 = int(words[4]), int(words[5])
        grid.loc[x1:x2, y1:y2] += 2
    else:
        x1, y1 = int(words[2]), int(words[3])
        x2, y2 = int(words[5]), int(words[6])
        if words[1] == 'on':
            grid.loc[x1:x2, y1:y2] += 1
        elif words[1] == 'off':
            grid.loc[x1:x2, y1:y2] -= 1

        negative_number = grid < 0
        grid[negative_number] = 0

for instruction in instructions:
    brightness(instructions)

total_brightness = grid.values.sum()
print("part2 total brightness:", total_brightness)