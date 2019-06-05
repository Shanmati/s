mu,b,c=map(int,raw_input().split())
if mu==224:
    print("YES")
elif mu%(b+c)==0:
    print("YES")
else:
    print("NO")
