with open('file.txt', 'r') as file:
    contents = file.read()

for i in range(len(contents)):    
    if line[0] != line[1] != line[2] != line[3]:
        #print index of last character
    else:
        line = contents[i:(i+4)]
    

print(line)
