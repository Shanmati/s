nu=int(input())
val=list(map(int,input().split()))
for i in val:
  if(val.count(i)==1):
    print(i)
    break
