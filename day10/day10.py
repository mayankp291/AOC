cycles = 0
x = 1
p1 = 0
G = [['?' for _ in range(40)] for _ in range(6)]
with open("day10/input.txt", "r") as f:
    def check():
        if cycles%40 == 20:
            global p1
            p1 += cycles*x
            print(cycles, p1, x)
        t1 = cycles - 1
        G[t1//40][t1%40] = ('#' if abs(x-(t1%40))<=1 else ' ')    

    for l in f:
        a = l.strip().split(" ")
        if a[0] == "noop": 
            cycles+=1
            check()
        if a[0] == "addx":
            cycles+=1
            check()
            cycles+=1
            check()
            x+=int(a[1])

print(x,cycles, p1)
for r in range(6):
    print(''.join(G[r]))


def maxStarSum(self, vals: List[int], edges: List[List[int]], k: int) -> int:
    # check each vertex and its adj edges
    res = set()
    for i,v in enumerate(vals):
        temp = 0
        for a in edges:
            if i in a:
                temp+= vals[i[1]]
        print(temp)