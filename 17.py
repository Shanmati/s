n=int(input())
m=n
if(n<=100000):
 remain=0
 while(n!=0):
  num=n%10
  remainder=remain+num*num*num
  n=n//10
 if(m==remain):
  print("yes")
 else:
  print("no")
