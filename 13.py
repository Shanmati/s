ac=int(input())
cd=0
if ac>1:
  for i in range(2,ac):
    if(ac %i)==0:
      print("no")
      break
    else:
      print("yes")
else:
  print("no")
