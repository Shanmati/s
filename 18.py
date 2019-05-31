h,k=list(map(int,input().split()))
for i in range(h,k):
    o=len(str(i))
    sumi=0
    r=i
    while(r>0):
       di=r% 10
       sumi+=di**o
       r//= 10
    if i==sumi:
        print(i,end=" ")
