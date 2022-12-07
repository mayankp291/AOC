import re
from collections import defaultdict

with open("day7/input.txt", "r") as f:
    lines = f.readlines()


dic = {}

        

# directory path -> total size of that directory (including subdirectories)
dic = defaultdict(int)
path = []
for line in lines:
    a = line.strip().split()
    if a[1] == "cd":
        if a[2] == "..":
            path.pop()
        else:
            path.append(a[2])
    elif a[1] == "ls" or a[0] == "dir":
        continue
    else:
        temp = int(a[0])
        for i in range(1, len(path)+1):
            p = '/'.join(path[:i])
            dic[p] += temp

print(dic)

part1 = 0
part2 = 1e9
max_used = 70000000 - 30000000
total_used = dic['/']
delete = total_used - max_used


for k,v in dic.items():
    if v <= 100000:
        part1+=v
    if v>=delete:
        part2 = min(v,part2)

print(part1)
print(part2)
