n,m=map(int,input().split())
a=[int(n) for n in input().split()]
b=[int(m) for m in input().split()]
cu=0
for i in range(0,len(b)):
    for j in range(0,len(a)):
        if b[i]==a[j]:
            cu +=1
if cu==len(b):
    print("YES")
else:
    print("NO")
