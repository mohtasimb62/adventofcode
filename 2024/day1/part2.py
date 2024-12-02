f = open("input", "r")

leftList = []
rightList = []

for line in f:
    splitted = line.split()

    leftList.append(int(splitted[0]))
    rightList.append(int(splitted[1]))


similarity = 0
for i in range(0, len(leftList)):
    count = 0 
    for j in range(0, len(rightList)):
        if rightList[j] == leftList[i]:
            count += 1
    
    similarity += leftList[i] * count

print(similarity)
