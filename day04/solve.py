import re

puzzle_input = open("data.txt", "r").read().rstrip().splitlines()

res1 = 0
res2 = 0

def count_ref(array) :
    res = 0
    for line in array :
        for match in re.finditer(r"XMAS", ''.join(line)):
            res += 1
        for match in re.finditer(r"SAMX", ''.join(line)):
            res += 1
    return res


largeur = len(puzzle_input[0])
vertical = [[puzzle_input[j][i] for j in range(largeur)] for i in range(largeur)]  #transpose le tableau
diagonal1 = [[puzzle_input[j][j-i] for j in range(i,largeur)] for i in range(largeur)]
diagonal2 = [[puzzle_input[j-i][j] for j in range(i,largeur)] for i in range(1,largeur)]
diagonal3 = [[puzzle_input[i-j-1][j] for j in range(i)] for i in range(largeur,0,-1)]
diagonal4 = [[puzzle_input[j][largeur-j+i-1] for j in range(largeur-1,i-1,-1)] for i in range(1,largeur)]

res1 += count_ref(puzzle_input)
res1 += count_ref(vertical)
res1 += count_ref(diagonal1)
res1+= count_ref(diagonal2)
res1 += count_ref(diagonal3)
res1+= count_ref(diagonal4)


for i,line in enumerate(puzzle_input) :
    for j,c in enumerate(line) :
        if c == 'A' and 0<i<len(line)-1 and 0<j<len(line)-1 :
            if (puzzle_input[i-1][j-1] == 'S' and puzzle_input[i+1][j+1]=='M') or (puzzle_input[i-1][j-1] == 'M' and puzzle_input[i+1][j+1]=='S') :
                if (puzzle_input[i+1][j-1] == 'S' and puzzle_input[i-1][j+1]=='M') or (puzzle_input[i+1][j-1] == 'M' and puzzle_input[i-1][j+1]=='S') :
                    res2 +=1


print("part 1 : ",res1)
print("part 2 : ",res2)