import re

f = open("input.txt", "r")

pattern = r"mul\((\d+),(\d+)\)"

count = 0
for line in f:
    matches = re.findall(pattern, line)
    for pair in matches:
        count += int(pair[0]) * int(pair[1])


print(count)