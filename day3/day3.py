res = 0
# f = open("day3/input.txt", "r")
# for i in f:
#     a = i.strip()
#     l = len(a)
#     b, c = a[:l//2], a[l//2:]
#     print(len(b),len(c))
#     d = ''.join(set(b).intersection(c))
#     print(b,c,d)
#     res += ord(d) - 64 + 26 if ord(d) < 97 else ord(d) - 96
# f.close()
# print(res)
with open("day3/input.txt", "r") as f:
    l = f.readlines()
i=0
while i+2 < len(l):
    d = ''.join(set(l[i]).intersection(l[i+1], l[i+2]))
    d = d.strip()
    print(d)
    res += ord(d) - 64 + 26 if ord(d) < 97 else ord(d) - 96
    i+=3
print(res)