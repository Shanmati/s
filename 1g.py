st1=input()
st1=list(st1)
for i in range(0,len(st1),2):
  st1[i],st1[i+1]=st1[i+1],st1[i]
print(''.join(st1))
