from itertools import combinations
mi,n=map(int,input().split())
h=len(str(mi))
len1=list(combinations(str(mi),h-n))
len1=sorted(len1)
print("".join(len1[0]))
