nu=int(input())
lo=[int(x) for x in input().split()]
lo.sort()
for i in range(nu) :
  print(lo[i],end=" ")
