with open('file.txt', 'r') as file:
    contents = file.read()

x = 0
y = 4
for i in range(len(contents)):
    line = contents[x:y]
    if line[0] not in line[1:4]:
        if line[1] not in (line[0] + line[2:4]):
            if line[2] not in (line[0:2] + line[3:4]):
                if line[3] not in (line[0:3]):
                    print('found it!')
                    print(y)
                    break
                else:
                    x += 1
                    y += 1
            else:
                x += 1
                y += 1
        else:
            x += 1
            y += 1
    else:
        x += 1
        y += 1

print(line)
