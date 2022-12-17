with open('file.txt', 'r') as file:
    contents = file.readlines()


score = 0
'''
#PART1
for line in contents: 
    if line[2] == 'X':
        score += 1
        if line [0] == 'A':
            score += 3
        elif line [0] == 'C':
            score += 6
            ###
    if line[2] == 'Y':
        score += 2
        if line [0] == 'A':
            score += 6
        elif line [0] == 'B':
            score += 3
            ###
    if line[2] == 'Z':
        score += 3
        if line [0] == 'B':
            score += 6
        elif line [0] == 'C':
            score += 3
'''
for line in contents:
    if line[2] == 'X':
        score += 0
        if line[0] == 'A':
            score += 3
        if line[0] == 'B':
            score += 1
        if line[0] == 'C':
            score += 2     
            ###
    if line[2] == 'Y':
        score += 3
        if line[0] == 'A':
            score += 1
        if line[0] == 'B':
            score += 2
        if line[0] == 'C':
            score += 3
            ###
    if line[2] == 'Z':
        score += 6
        if line[0] == 'A':
            score += 2
        if line[0] == 'B':
            score += 3
        if line[0] == 'C':
            score += 1
print(score)
