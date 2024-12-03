import re

puzzle_input = open("data.txt", "r").read().rstrip().splitlines()

res1 = 0
res2 = 0

mult = 1
for line in puzzle_input :
    for match in re.finditer(r"(mul\((\d+),(\d+)\))|(do\(\))|(don't\(\))", line):
            if match.group(0) == "do()" :
                mult = 1
            elif match.group(0) == "don't()" :
                mult = 0
            else :
                res1 += int(match.group(2))*int(match.group(3))
                res2 += mult * int(match.group(2))*int(match.group(3))

print("part 1 : ",res1)
print("part 2 : ",res2)