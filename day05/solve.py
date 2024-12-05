from collections import defaultdict

puzzle_input = open("data.txt", "r").read().rstrip().split("\n\n")
res1 = 0
res2 = 0


rules = puzzle_input[0].splitlines()
pages = puzzle_input[1].splitlines()

rules_dic = defaultdict(list)
for line in rules :
    prec,next = line.split('|')
    rules_dic[prec].append(next)

wrong = []

#part 1
for line in pages :
    values = line.split(',')

    isOK = True
    for index,value in enumerate(values) :
        if value in rules_dic :
            for rule in rules_dic[value] :
                if rule in values[:index] :
                    isOK = False

    if isOK :
        res1+=int(values[len(values)//2])
    else :
        wrong.append(values)


#part 2
for values in wrong :
    isOk = False
    while not isOk :
        isOk=True
        for index,value in enumerate(values) :
            if value in rules_dic :
                for rule in rules_dic[value] :
                    if rule in values[:index] :
                    #si placé trop loin on permute
                        isOk=False
                        indexToPlace = values.index(rule)
                        values[index]=rule
                        values[indexToPlace]=value
                        break

    res2+=int(values[len(values)//2])
print("part 1 : ",res1)
print("part 2 : ",res2)