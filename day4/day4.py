# PART 1
# res = 0
# f = open("day4/input.txt", "r")
# for i in f:
#     a = i.strip().split(",")
#     b = [int(x) for x in a[0].split("-")]
#     c = [int(x) for x in a[1].split("-")]
#     print(a, b, c)
#     # b contained in c
#     if b[1] <= c[1] and b[0] >= c[0]:
#         res+=1
#     # c contained in b
#     elif b[1] >= c[1] and b[0] <= c[0]:
#         res+=1
# f.close()
# print(res)

# PART 2
res = 0
f = open("day4/input.txt", "r")
for i in f:
    a = i.strip().split(",")
    b = [int(x) for x in a[0].split("-")]
    c = [int(x) for x in a[1].split("-")]
    print(a, b, c)
    # 3 TYPES OF OVERLAP - FULL, LEFT, RIGHT
    # FULL
    # b contained in c
    if b[1] <= c[1] and b[0] >= c[0]:
        res+=1
    # c contained in b
    elif b[1] >= c[1] and b[0] <= c[0]:
        res+=1
    # LEFT
    elif b[0] <= c[1] <= b[1] or c[0] <= b[1] <= c[1] :
        res+=1
    # RIGHT
    elif b[0] <= c[0] <= b[1] or c[0] <= b[0] <= c[1] :
        res+=1    
f.close()
print(res)
