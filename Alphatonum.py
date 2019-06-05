ni=input()
c=1
for i in range(len(ni)-1):
    a=ni[i]+ni[i+1]
    b=int(a)
    if b<=26 and ni[i]!="0":
        c+=1
if c==3:
    print(c)
else:
    print(c+(c-1)//2)
