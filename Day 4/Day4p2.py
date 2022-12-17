with open('file.txt', 'r') as file:
    contents = file.readlines()

counter = 0
for line in contents:
    lst = line.split(',')
    part1 = lst[0].split('-')
    part2 = lst[1].replace('\n', '').split('-')
    if int(part2[0]) <= int(part1[1]) <= int(part2[1]):
        counter += 1
    elif int(part2[0]) <= int(part1[0]) <= int(part2[1]):
        counter += 1
    elif int(part1[0]) <= int(part2[1]) <= int(part1[1]):
        counter += 1
    elif int(part1[0]) <= int(part2[0]) <= int(part1[1]):
        counter += 1
print(counter)

