ac=input()
c=0
d=len(ac)
for i in range (d):
  if((int(ac[0+i]))==(int(ac[d-1-i]))):
    c=c+1
  else:
    c=c-1
if(c==d):
  print("yes")
else:
  print("no")
