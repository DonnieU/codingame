# THEY put you in a square shape room, with N meters on each side.
# THEY want to know everything about you.
# THEY are observing you.
# THEY placed some candles in the room.

# Every candle makes L "light" in the spot they are, and every spot
# in square shape gets one less "light" as the next ones. If a spot is
# touched by two candles, it will have the larger "light" it can have.
# Every spot has the base light of 0.

# You can hide only, if you find a dark spot which has 0 "light".
# How many dark spots you have?

# You will receive a map of the room, with the empty places (X)
# and Candles (C) in N rows, each character separated by a space.

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

# CONSTRAINTS:
# 0<N<=25
# 0<L<10

import math
src = ['X X X X X', 'X C X X X', 'X X X X X', 'X X X X X', 'X X X X X']
n = 5
l = 3
# EXPECTED RESULT FROM SRC: 9

"""
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
"""

# Large room...
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
# EXPECTED RESULT FROM SRC: 

""" THIS WORKS BUT FAILS THE BEHIND-THE-SCENES VALIDATORS """

# Creates 2D list of n elements sublists from src
room = [line.split(' ') for line in src]

print('room:')
print(room)

# List of zeroes
lit = [0]*n*n # use when using [loc]

print(lit)
print()

def dist(x,y,row,col):
    # d = math.sqrt((row - y)**2 + (col - x)**2)
    d = l
    a = abs(row-y)
    b = abs(col-x)
    if a<l and b<l:
        d = max(a,b)
    return d

def calc_light(row, col):
    for y in range(n):
        for x in range(n):
            distance = dist(x,y,row,col)
            val = l - distance
            if val > 0:
                loc = x + y*n
                lit[loc] = lit[loc] + val


for col in range(len(room)):
    for row in range(len(room)):
        if room[row][col] == 'C':
            calc_light(row, col)

print(lit)

zeroes = 0

zeroes = lit.count(0)

print('zeroes: {}'.format(zeroes))
