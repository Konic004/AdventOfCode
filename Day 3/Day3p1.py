with open('file.txt', 'r') as file:
    contents = file.readlines()
score = 0
for line in contents:
    half = int(len(line) / 2)
    part1 = line[:half]
    part2 = line[half:]
    for i in range(65, 123):
        if chr(i) in part1 and chr(i) in part2:
            if 65 <= i <= 90:
                score += (i - 38)
            else:
                score += (i - 96)
print(score)
