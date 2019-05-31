zaw=int(input())
a=zaw
s=0
while zaw>0:
    r=zaw%10
    s=s+r**3
    za=zaw//10
if s==a:
    print("yes")
else:
    print("no")
