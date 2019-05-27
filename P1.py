su=input()
su=int(su)
l=[]
for i in range(0,su):
    s1=input()
    l.append(s1)
Z=[]
for i in zip(*l):
    if i.count(i[0])==len(i):
        Z.append(i[0])
    else:
        break
print(''.join(Z))
