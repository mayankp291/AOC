arr = [['B', 'S', 'V', 'Z', 'G','P','W'],
        ['J', 'V', 'B', 'C', 'Z', 'F'],
        ['V', 'L', 'M', 'H', 'N', 'Z', 'D', 'C'],
        ['L', 'D', 'M', 'Z', 'P', 'F', 'J', 'B'],
        ['V', 'F', 'C', 'G', 'J', 'B', 'Q', 'H'],
        ['G', 'F', 'Q', 'T', 'S', 'L', 'B'],
        ['L', 'G', 'C', 'Z', 'V'],
        ['N', 'L', 'G'],
        ['J', 'F', 'H', 'C']]

# # PART 2
res = 0
file = open("day5/input.txt", "r")
for i in file:
    temp = []
    a = i.strip().split(" ")
    loop = int(a[1])
    f = int(a[3])
    t = int(a[-1])
    print(loop, f, t)
    k = loop
    while k:
        temp.append(arr[f-1].pop())
        k-=1
    while loop:
        arr[t-1].append(temp.pop())
        loop-=1
print(arr)   
file.close()
for i in range(9):
    print(arr[i].pop())
print(res)
