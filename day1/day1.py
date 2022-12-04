res = []

f = open("input.txt", "r")
temp = 0
for i in f:
    if not i.strip():
        print("Sum:", temp)
        res.append(temp)
        temp = 0
    else:
        temp+= int(i.strip())

f.close()
res.sort()
print("Result", sum(res[-3:]))