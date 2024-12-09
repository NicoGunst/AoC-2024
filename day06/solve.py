import copy

puzzle_input = open("data.txt", "r").read().rstrip().split("\n")
res1 = 0
res2 = 0

height = len(puzzle_input)
width = len(puzzle_input[0])

def find_guard(array) :
    for i,line in enumerate(array) :
        for j,value in enumerate(line) :
            if value in '<>^v' :
                return (i,j)
    return (-1,-1)

def next_pos(guard_char) :
    match guard_char :
        case '^':
            return (-1,0)
        case '>':
            return (0,1)
        case '<':
            return (0,-1)
        case 'v':
            return (1,0)
        case '_':
            return (0,0)

def turn_right(guard_char) :
    match guard_char :
        case '^':
            return '>'
        case '>':
            return 'v'
        case '<':
            return '^'
        case 'v':
            return '<'
        case '_':
            return 'E'

pos = []
#part 1
for line in puzzle_input :
    pos.append([value for value in line])

init_pos = copy.deepcopy(pos)

out = False
visited = set()
init_guard = find_guard(pos)
init_guard_direction = pos[init_guard[0]][init_guard[1]]
x,y = init_guard
while not out :
    if (x,y) == (-1,-1) :
            out = True
            continue
    nextX,nextY = next_pos(pos[x][y])
    oldGuard = pos[x][y]
    pos[x][y] = '.'
    visited.add((x,y))
    x,y = (x+nextX,y+nextY)
    if  0<= x < height and 0<= y < width :
        if pos[x][y] == '.' :
            pos[x][y] = oldGuard
        else :
            x,y = x-nextX,y-nextY
            pos[x][y] = turn_right(oldGuard)
    else :
        x,y = (-1,-1)
res1 = len(visited)

#Part 2
for elem in visited :
    visited_direction = set()
    pos = copy.deepcopy(init_pos)
    if not elem == init_guard :
        pos[elem[0]][elem[1]] = '#'
    x,y = x,y = init_guard
    out = False
    while True :
        while not out :
            if (x,y) == (-1,-1) :
                out = True
                continue
            nextX,nextY = next_pos(pos[x][y])
            oldGuard = pos[x][y]
            pos[x][y] = '.'
            pos_direction = (x,y,oldGuard)
            if (pos_direction in visited_direction) :
                out = True
                res2 += 1
                break
            visited_direction.add(pos_direction)
            x,y = (x+nextX,y+nextY)
            if  0<= x < height and 0<= y < width :
                if pos[x][y] == '.' :
                    pos[x][y] = oldGuard
                else :
                    x,y = x-nextX,y-nextY
                    pos[x][y] = turn_right(oldGuard)
            else :
                x,y = (-1,-1)
        res1 = len(visited)
        break


print("part 1 : ",res1)
print("part 2 : ",res2)