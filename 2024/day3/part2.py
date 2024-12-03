import re

f = open("input.txt", "r")

# patternForMulPhrases = r"mul\((\d+),(\d+)\)"
# patternForDoAndDont = r"(?:do|don't)\(\)"
combinedPattern = r"(do\(\)|don't\(\)|mul\((\d+),(\d+)\))"


flag = 1
count = 0

for line in f:
    matches = re.findall(combinedPattern, line)
    for pair in matches:
        if pair[0] == "don't()":
            flag = 0
        elif pair[0] == "do()":
            flag = 1
        else:
            if flag != 0:
                count += int(pair[1]) * int(pair[2])


print(count)