nu=input()
l=['1','2','3','4','5','6','7','8','9','0','.']
c=0
for i in nu :
  if i not in l :
    c=c+1
if c==0 :
  print("yes")
else :
  print("No")
