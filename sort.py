nk=int(input ())
l1=list(map(int,input().split())
t=[]
for i in l1:
  if(l1.count(i)>1):
    t.append(i)
a=set(t)
if len(a) ==0:
  print("unique")
else:
  print(*a)
