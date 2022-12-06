from collections import Counter

# PART 1
# with open("day6/input.txt", "r") as f:
#     l = f.readline()
#     for i in range(len(l)-3):
#         s = l[i:i+4]
#         if len(Counter(s)) == len(s):
#             print(i+4)
#             break

# PART 2
with open("day6/input.txt", "r") as f:
    l = f.readline()
    for i in range(len(l)-13):
        s = l[i:i+14]
        if len(Counter(s)) == len(s):
            print(i+14)
            break
        

