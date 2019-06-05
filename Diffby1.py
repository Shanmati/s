a,b=input().split()
ci=0
for i in range(len(a)):
    if a[i]==b[i]:
        continue
    else:
        ci+=1
if ci==1:
    print("yes")
else:
    print("no")
