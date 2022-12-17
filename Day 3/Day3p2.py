with open('file.txt', 'r') as file:
    contents = file.readlines()
score = 0
for i in range(0, len(contents) - 1, 3):
    line1 = contents[i]
    line2 = contents[i + 1]
    line3 = contents[i + 2]
    for i in range(65, 123):
        if chr(i) in line1 and chr(i) in line2 and chr(i) in line3:
            if 65 <= i <= 90:
                score += (i - 38)
            else:
                score += (i - 96)
print(score)
