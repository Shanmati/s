N1,K=map(int,input().split())
AC=list(map(int,input().split()))

B=set(AC)
BBB=sorted(B, reverse=False)
C=list(BBB)

print(C[-K])
