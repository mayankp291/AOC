monkey = [x for x in range(8)]
inspect = [0]*8
items = [[66, 71, 94], [70], [62, 68, 56, 65, 94, 78], 
        [89, 94, 94, 67], [71, 61, 73, 65, 98, 98, 63],
        [55, 62, 68, 61, 60], [93, 91, 69, 64, 72, 89, 50, 71],
        [76, 50]]

def test(x,i):
    if i==0: return x*5
    if i==1: return x+6
    if i==2: return x+5
    if i==3: return x+2
    if i==4: return x*7
    if i==5: return x+7
    if i==6: return x+1
    if i==7: return x*x

T = [7,3,3,7,5,2,5,4]
F = [4,0,1,0,6,1,2,6]
div = [3,17,2,19,11,5,13,7]

# MATH HACK
# Want to know for each item if it is divisible by e.g. 23,19,13,17
# If we just wanted to know if its divisible by 23, we can just keep track of the number modulo 23.
# x+a is divisible by 23 iff (x%23)+a is divisible by 23
# x*a is divisible by 23 iff (x%23)*a is divisible by 23
# We can keep track of the number modulo 23*19*13*17
lcm = 1
for x in div:
    lcm = (lcm*x)

print(items)
for _ in range(10000):
    for i in monkey:
        while items[i]:
            stress = items[i].pop(0)
            stress = test(stress,i)
            ## PART 1
            # stress = stress // 3
            ## PART 2
            stress %= lcm
            inspect[i] += 1
            if stress%div[i] == 0:
                items[T[i]].append(stress)
            else:
                items[F[i]].append(stress)

# print(items)
print(inspect)
print(sorted(inspect)[-1]*sorted(inspect)[-2])
