f = open("input.txt", "r")

def increasing(list):
    for i in range(1, len(list)):
        if list[i] < list[i-1] or abs(list[i]-list[i-1]) < 1 or abs(list[i]-list[i-1]) > 3:
            return False
    return True

def decreasing(list):
    for i in range(1, len(list)):
        if list[i] > list[i-1] or abs(list[i]-list[i-1]) < 1 or abs(list[i]-list[i-1]) > 3:
            return False
    return True

def problemDampener():
    pass


def removeElement(list, index):
    newList = []                # new list with the requested index element removed 
    for i in range(0, len(list)):
        if i != index:
            newList.append(list[i])
    return newList



count = 0 # to keep track of the safe levels
for line in f:
    splittedLine = list(map(int, line.strip().split()))
    toleratedCount = 0

    for i in range(0, len(splittedLine)):
        toleratedList = removeElement(splittedLine, i)

        if increasing(toleratedList) or decreasing(toleratedList):
            toleratedCount += 1
    
    if toleratedCount > 0:
        count+=1
        

print(count)