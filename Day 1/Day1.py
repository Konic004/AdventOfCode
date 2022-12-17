with open('file.txt', 'r') as file:
    contents = file.read()
    info = contents.split('\n\n') #splitting file into the elf groups


valuelist = [i.split('\n') for i in info] #creating a list of calorie values for each elf element

for idx, i in enumerate(valuelist): #converting calorie values to integers
    valuelist[idx] = [int(j) for j in i]

sumlist = [sum(i) for i in valuelist] #list of all the sums of calories for the elves
maximum1 = max(sumlist)
sumlist.remove(maximum1)
maximum2 = max(sumlist)
sumlist.remove(maximum2)
maximum3 = max(sumlist)
supermax = maximum1 + maximum2 + maximum3
print(supermax)
