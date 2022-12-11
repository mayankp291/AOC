import numpy as np
from collections import Counter

head = (200,200)
tail = (200,200)
dir = {'U':(0,1), 'D': (0,-1), 'L':(-1,0), 'R': (1,0)}
grid = np.zeros((400,400), dtype=int)
grid[tail] = 1

def chebyshev_dist(a, b):
    return max(abs(a[1] - b[1]), abs(a[0] - b[0]))

with open("day9/input.txt", "r") as f:
    for l in f:
        # l = f.readline()
        a = l.strip().split(" ")
        # print(a)
        d, v = a[0], int(a[1])
        x, y = dir[d][0], dir[d][1]
        # with each move check adj of tail and move
        while v > 0:
            head = (head[0]+x, head[1]+y)
            while chebyshev_dist(head, tail) > 1:
                a = [-1,0,1]
                dist = 4
                res = (0,0)
                for i in a:
                    for j in a:
                        temp = (tail[0]+i, tail[1]+j)
                        if chebyshev_dist(head, temp) < dist:
                            dist = chebyshev_dist(head, temp)
                            res = temp
                tail = res
                # tail = (tail[0]+x, tail[1]+y)
                grid[tail] = 1
            v-=1
        # print(head) 

print(grid)
print((grid == 1).sum())

def tail_move(h, t):
    d = h - t
    if any(np.abs(d) == 2):
        t += np.sign(d)  
    return t

h_t = np.zeros((10,2)) # Position 0 is head 1-9 the tails
visited_1 = set()
visited_9 = set()

direction_to_grid = {"R": [1,0], "L": [-1,0], "U": [0,1], "D": [0,-1]}
for line in open("day9/input.txt"):
    direction, steps = line.split(" ")
    for _ in range(int(steps)): 
        h_t [0] += direction_to_grid[direction]
        for t in range(1, len(h_t )):
            h_t [t] = tail_move(h_t [t-1], h_t [t])

        visited_1.add(str(h_t [1,0]) + "_" + str(h_t [1,1]))
        visited_9.add(str(h_t [9,0]) + "_" + str(h_t [9,1]))
print(len(visited_1), len(visited_9))