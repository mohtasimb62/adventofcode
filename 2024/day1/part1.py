f = open("input", "r")

leftList = []
rightList = []

for line in f:
    splitted = line.split()

    leftList.append(int(splitted[0]))
    rightList.append(int(splitted[1]))

leftList = sorted(leftList)
rightList = sorted(rightList)

total = 0
for i in range(0, len(leftList)):
    total += abs(leftList[i] - rightList[i])

print(total)
