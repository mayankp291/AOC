import numpy as np

with open("day8/input.txt", "r") as f:
    lines = f.readlines()

arr = np.empty([99,99], dtype=int)
check = np.zeros((99,99), dtype=int)
i = j = 0
for l in lines:
    j=0
    for c in l.strip():
        arr[i][j] = int(c)
        j+=1
    i+=1

check[0] = 1
check[-1] = 1
check[:,0] = 1
check[:,-1] = 1

# PART 1
for i in range(1,98):
    for j in range(1,98):
        if max(arr[i,:j]) < arr[i,j] or max(arr[i,j+1:]) < arr[i,j]:
            check[i,j] = 1

for j in range(1,98):
    for i in range(1,98):
        if max(arr[:i,j]) < arr[i,j] or max(arr[i+1:,j]) < arr[i,j]:
            check[i,j] = 1


print((check == 1).sum())

scenic = np.zeros((99,99), dtype=int)
p2 = 0

# PART 2
dir = [(-1,0),(0,1),(1,0),(0,-1)]
for i in range(99):
    for j in range(99):
        dist = 1
        for (x,y) in dir:
            temp = 1
            r,c = i+x, j+y
            while True:
                if not (0<=r<99 and 0<=c<99):
                    temp -= 1
                    break
                if arr[r,c] >= arr[i,j]: break
                temp += 1
                r += x
                c += y
            dist *= temp    
        scenic[i,j] = dist
        
print(np.amax(scenic))
