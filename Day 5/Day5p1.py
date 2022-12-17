with open('stack.txt', 'r') as stack:
    contents = stack.readlines()
    stackd = {
                1 : [],
                2 : [],
                3 : [],
                4 : [],
                5 : [],
                6 : [],
                7 : [],
                8 : [],
                9 : []
              }
    for line in contents: #iterating through each line
        if '1' not in line: #making sure we're not on the bottom line (don't know how else to check this :P)
            column = 1
            for i in range(1, 36, 4): #iterating through the values in the columns (they're separated by 4 characters)
                if line[i] != ' ' and column < 10: #not adding empty vals, and making sure the column doesnt go too high
                    stackd[column].append(line[i]) #adding the val to list!! :)
                column += 1 #increasing column value


with open('instructions.txt', 'r') as instr:
    contents = instr.readlines()
    for line in contents:
        splitline = line.split()
        numcrates = int(splitline[1])
        losecolumn = int(splitline[3])
        gaincolumn = int(splitline[5])
        for i in range(numcrates):
            crate = stackd[losecolumn].pop(0)
            stackd[gaincolumn].insert(0, crate)

for key, value in stackd.items():
    print(key, value[0])
