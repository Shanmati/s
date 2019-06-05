m,n=input().split()
ob=abs(len(m)-len(n))
for i in range(len(m)):
	if len(n)==1 and n[i] in m:
		break
	elif i>=len(m) or i>=len(n):
		break
	elif n[i]!=n[i] and n[i]:
		ob=ob+1
print(ob)
