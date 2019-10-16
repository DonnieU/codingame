# THEY put you in a square shape room, with N meters on each side.
# THEY want to know everything about you.
# THEY are observing you.
# THEY placed some candles in the room.

# Every candle makes L "light" in the spot they are, and every spot in square shape gets one less "light" as the next ones. If a spot is touched by two candles, it will have the larger "light" it can have. Every spot has the base light of 0.

# You can hide only, if you find a dark spot which has 0 "light".
# How many dark spots you have?

# You will receive a map of the room, with the empty places (X) and Candles (C) in N rows, each character separated by a space.

# Example for the light spread N = 5, L = 3:
# INPUT:
# 5
# 3
# X X X X X
# X C X X X
# X X X X X
# X X X X X
# X X X X X

# 2 2 2 1 0
# 2 3 2 1 0
# 2 2 2 1 0
# 1 1 1 1 0
# 0 0 0 0 0

# OUTPUT:
# 9

import math
src = ['X X X X X', 'X C X X X', 'X X X X X', 'X X X X X', 'X X X X X']

n = 5
l = 3

# Test of large room w/ different C locations...
src = ['X X X C X C X X X X X X X X X X X X X X',
'X C X X X C X X X X C X X X X C X X X X',
'X X X X X X X X X X X X X C C X X X X X',
'X X X X X X X X X X X X X X X X X X X X',
'X X X X X X X X X X X X X X X X X X X C',
'X X X X X X X X C X X X X X X X C X X X',
'X X X X X C X X X X X X X X C X X X X C',
'X X X X X X C X X C C C X X X X X X X X',
'X C X X X X X X X X C X X X C X X X X X',
'X X X X C X X C X X X X X X X X X C X X',
'X X X X X X X X X C X C X X X X X X X X',
'X X X X X X X X X X X X X X X X X X X X',
'X X X X X X C X X X X X X X X X X C X X',
'X X X X X X X X X X X X X X X X X X X X',
'X X X X X X X X X C C X X X X C X X X X',
'X X X X X X X X X X X X C C C X X X X X',
'X X X X X X X X C X X X X X X X C C X X',
'X X X C X X X X X X X X X X X X X C X X',
'X X X X X C X X X X X X X X X C X X X X',
'X C X C X X X X X X X X X X X X X X X X']
n = 20
l = 3
# EXPECTED RESULT FROM SRC: 34

# Medium room...
src = ['X X X X X X X X X X X X C X X',
'X X X X X X X X X X X X C X X',
'X X X X X X X X X C X X X X X',
'X X X X X C X X X X X X X X X',
'X X X X C X X X X X X X X X X',
'C X X X X X X X C X X C X X X',
'X X X X X C X X X X X X X X C',
'X C X X X X X X X X X X X X X',
'X X X X X X X C X C X X X X X',
'X X X X X X X X X X X X C X X',
'X X X X X X X X X X X X X X X',
'X X C X C X X X X X X X X X C',
'X X X X X X C X X X C X X X X',
'X C X X X X X X X X X X X X X',
'X X X X X X X X X X X X X X X']
n = 15
l = 3
# EXPECTED RESULT FROM SRC: 14

src = ['C X X X X X X X X X X X X X X',
'X X X X X X X X X X X X X X X',
'X X X X X X X X X X X X X X X',
'X X X X X X X X X X X X X X X',
'X X X X X X X X X X X X X X X',
'X X X X X X X X X X X X X X X',
'X X X X X X X X X X X X X X X',
'X X X X X X X C X X X X X X X',
'X X X X X X X X X X X X X X X',
'X X X X X X X X X X X X X X X',
'X X X X X X X X X X X X X X X',
'X X X X X X X X X X X X X X X',
'X X X X X X X X X X X X X X X',
'X X X X X X X X X X X X X X X',
'X X X X X X X X X X X X X X X']
n = 15
l = 6

"""
If l = 6 and when using Euclidian distance,
this is the resulting matrix:
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
[0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0]
[0, 0, 0, 1, 1, 2, 2, 2, 2, 2, 1, 1, 0, 0, 0]
[0, 0, 1, 1, 2, 3, 3, 3, 3, 3, 2, 1, 1, 0, 0]
[0, 0, 1, 2, 3, 4, 4, 4, 4, 4, 3, 2, 1, 0, 0]
[0, 0, 1, 2, 3, 4, 5, 5, 5, 4, 3, 2, 1, 0, 0]
[0, 0, 1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 0, 0]
[0, 0, 1, 2, 3, 4, 5, 5, 5, 4, 3, 2, 1, 0, 0]
[0, 0, 1, 2, 3, 4, 4, 4, 4, 4, 3, 2, 1, 0, 0]
[0, 0, 1, 1, 2, 3, 3, 3, 3, 3, 2, 1, 1, 0, 0]
[0, 0, 0, 1, 1, 2, 2, 2, 2, 2, 1, 1, 0, 0, 0]
[0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0]
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

but what we want is:
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
[0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0]
[0, 0, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 0, 0]
[0, 0, 1, 2, 3, 3, 3, 3, 3, 3, 3, 2, 1, 0, 0]
[0, 0, 1, 2, 3, 4, 4, 4, 4, 4, 3, 2, 1, 0, 0]
[0, 0, 1, 2, 3, 4, 5, 5, 5, 4, 3, 2, 1, 0, 0]
[0, 0, 1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 0, 0]
[0, 0, 1, 2, 3, 4, 5, 5, 5, 4, 3, 2, 1, 0, 0]
[0, 0, 1, 2, 3, 4, 4, 4, 4, 4, 3, 2, 1, 0, 0]
[0, 0, 1, 2, 3, 3, 3, 3, 3, 3, 3, 2, 1, 0, 0]
[0, 0, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 0, 0]
[0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0]
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

then use the method in the def dist function below...
"""

""" This method worked!!! """
room = [line.split(' ') for line in src]
for r in room:
    print(r)
print()

lit = []
for i in range(n):
    lit.append([0]*n)


def dist(x, y, row, col):
    # d = math.sqrt((row-y)**2 + (col-x)**2)
    # return int(d)
    d = l
    a = abs(row-y)
    b = abs(col-x)
    if a<l and b<l:
        d = max(a,b)

    return d

def calc_light(row, col):
    for y in range(len(room)):
        for x in range(len(room)):
            distance = dist(x,y,row,col)
            val = l - distance
            # if val > 0:
            if val > lit[x][y]:
                 # lit[x][y] = lit[x][y] + val
                 lit[x][y] = val


for col in range(len(room)):
    for row in range(len(room)):
        if room[row][col] == 'C':
            calc_light(row,col)

# print(lit)
for l in lit:
    print(l)

zeroes = 0

for row in range(len(lit)):
    zeroes = zeroes + lit[row].count(0)

print('zeroes: {}'.format(zeroes))
