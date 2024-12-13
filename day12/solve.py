import sys
from collections import defaultdict
sys.setrecursionlimit(20000)

puzzle_input = open("data.txt", "r").read().rstrip().split("\n")
res1 = 0
res2 = 0

direction = {
    (-1,0),
    (0,1),
    (1,0),
    (0,-1)
}

garden = [[letter for letter in line] for line in puzzle_input]
h,w = len(garden),len(garden[0])
index_region = [[-1]*w for _ in range(h)]
regions = {}
def search_region(i,j,garden,index_region,z,char) :
    if not (0<=i<h and 0<=j<w) :
        return
    if index_region[i][j] != -1 :
        return
    if garden[i][j] == char :
        index_region[i][j]=z
        for d in direction :
            search_region(i+d[0],j+d[1],garden,index_region,z,char)

def count_perimeter(pos,region):
    i,j = pos
    res = 0
    for d in direction :
        new_i = i+d[0]
        new_j = j+d[1]
        if 0<=new_i<h and 0<=new_j<w :
            if (new_i,new_j) not in region :
                res += 1
        else :
            res += 1
    return res

def count_corner(pos,region):
    i,j = pos
    res = 0
    res += (i-1,j) not in region and (i,j-1) not in region
    res += (i+1,j) not in region and (i,j-1) not in region
    res += (i-1,j) not in region and (i,j+1) not in region
    res += (i+1,j) not in region and (i,j+1) not in region
    res += (i-1,j) in region and (i,j-1) in region and (i-1,j-1) not in region
    res += (i+1,j) in region and (i,j-1) in region and (i+1,j-1) not in region
    res += (i-1,j) in region and (i,j+1) in region and (i-1,j+1) not in region
    res += (i+1,j) in region and (i,j+1) in region and (i+1,j+1) not in region
    return res


#identify regions
index_reg = 0
for i in range(h):
    for j in range(w) :
        if index_region[i][j] == -1 :
            search_region(i,j,garden,index_region,index_reg,garden[i][j])
            index_reg += 1

#group regions in set
regions = defaultdict(set)
for i in range(h):
    for j in range(w) :
        regions[index_region[i][j]].add((i,j))

print(regions)

for region in regions.values() :
    perim = 0
    corner = 0
    for elem in region :
        perim+= count_perimeter(elem,region)
        corner+= count_corner(elem,region)
    res1 += len(region)*perim
    res2 += len(region)*corner



print("part 1 : ",res1)
print("part 2 : ",res2)