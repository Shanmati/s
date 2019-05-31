x,y=input().split()
ab=int(x)
bx=int(y)
for i in range(ab+1,bc):
    if(i>1):
        for j in range(2,i//2 + 1):
            if(i%j==0):
                break
        else:
            print(i,end=' ')
    else:
        break
