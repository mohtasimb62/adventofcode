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


count = 0 # to keep track of the safe levels
for line in f:
    splitted = list(map(int, line.strip().split()))

    if increasing(splitted) or decreasing(splitted):
        count += 1

print(count)