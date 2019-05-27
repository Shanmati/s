nu=int(input())
li=[]
for i in range(n):
  li.append(input())
minilen=len(min(li,key=len))
for i in range(len(li)-1):
  for j in range(minilen):
    if li[i][:j+1] in li[i+1]:
      t=li[i][:j+1]
print(t)
