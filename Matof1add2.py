n=int(input())
li=[int(x) for x in input().split()]
s=[]
for i in range(0,len(li)):
	for j in range(i+1,len(li)):
		for k in range(j+1,len(li)):
			if li[i]+li[j]==li[k]:
				s.append(li[k])
				print(li[i],li[j],li[k])
				break
