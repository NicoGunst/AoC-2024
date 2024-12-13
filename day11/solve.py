import functools

puzzle_input = open("data.txt", "r").read().rstrip()
res1 = 0
res2 = 0

stones = [int(x) for x in puzzle_input.split(' ')]


def blink(stone) :
    if stone == 0:
        return [1]
    s = str(stone)
    l = len(s)
    if l%2 == 0 :
        return [int(s[:(l//2)]),int(s[l//2:])]
    return [stone*2024]

@functools.cache
def rec_count(stones,blink_num):
    if blink_num == 0:
        return len(stones)
    return sum(rec_count(tuple(blink(stone)),blink_num-1) for stone in stones)

for stone in stones :
    sub_stones = [stone]
    res1+= rec_count(tuple(sub_stones),25)

print("part 1 : ",res1)

for stone in stones :
    sub_stones = [stone]
    res2+= rec_count(tuple(sub_stones),75)


print("part 2 : ",res2)