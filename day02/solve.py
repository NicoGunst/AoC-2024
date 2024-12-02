puzzle_input = open("data.txt", "r").read().rstrip().splitlines()

res1 = 0
res2 = 0

def isReportOK(report) :
    diff = [j-i for i, j in zip(report[:-1], report[1:])]
    isOk=True
    for index,value in enumerate(diff):
        if index > 0 and value * diff[index-1] < 0 :
            isOk=False
            continue
        if not (1 <= abs(value) <= 3) :
            isOk=False
            continue
    return isOk

for line in puzzle_input :
    elt = list(map(int,line.split(' ')))
    if isReportOK(elt) :
        res1 += 1
        res2 += 1
    else :
        for i in range(len(elt)) :
            report = elt[:i] + elt[i+1:]
            if isReportOK(report) :
                res2 +=1
                break



print("part 1 : ",res1)
print("part 2 : ",res2)