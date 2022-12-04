score = 0
f = open("Day 2/input.txt", "r")
temp = 0
d = {'A': 1, 'B': 2, "C": 3}
lose = {'A': 3, 'B': 1, 'C': 2}
win = {'A': 2, 'B': 3, 'C': 1}
for i in f:
    a = i.strip()
    a = a.split(" ")
    print(a[0], a[1])
    if a[1] == 'Y': score += 3 + d[a[0]]
    elif a[1] == 'X': score += lose[a[0]]   
    elif a[1] == 'Z': score += 6 + win[a[0]]
    # ABC XYZ rock paper scissor
    
f.close()
print(score)