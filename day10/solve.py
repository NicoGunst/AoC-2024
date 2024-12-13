puzzle_input = open("data.txt", "r").read().rstrip().split("\n")
res1 = 0
res2 = 0

data = [[int(x) for x in line] for line in puzzle_input]
height = len(data)
width = len(data[0])

direction={
    (-1,0),
    (0,1),
    (1,0),
    (0,-1)
}

def rec_search(i,j,data,target) :
    if not(0<=i<height and 0<=j<width) :
        return set()
    if data[i][j] != target:
        return set()
    if data[i][j] == 9:
        return {(i,j)}
    res = set()
    for d in direction:
        res=res.union(rec_search(i+d[0], j+d[1],data, target+1))
    return res

def rec_search_part2(i,j,data,target) :
    if not(0<=i<height and 0<=j<width) :
        return list()
    if data[i][j] != target:
        return list()
    if data[i][j] == 9:
        return [(i,j)]
    res = list()
    for d in direction:
        res+=(rec_search_part2(i+d[0], j+d[1],data, target+1))
    return res

for i,line in enumerate(data):
    for j,point in enumerate(line):
        if point==0:
            res1+=len(rec_search(i,j,data,0))
            res2+=len(rec_search_part2(i,j,data,0))


print("part 1 : ",res1)
print("part 2 : ",res2)