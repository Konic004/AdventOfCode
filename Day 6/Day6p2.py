with open('file.txt', 'r') as file:
    contents = file.read()

x = 0
y = 14
for i in range(len(contents)):
    line = contents[x:y]
    if len(set(line)) == 14:
        print(y)
        break
    else:
        x += 1
        y += 1

print(line)
