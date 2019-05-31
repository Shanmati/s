nu=int(input())
l=[int(x) for x in input().split()]
m=l[0]
for i in range(0,nu):
    if(m>l[i]):
        m=l[i]
print(m)
