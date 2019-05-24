a=input()
d=0
f=len(a)
if(ord(a[0])<57):
	if(ord(a[0])>47 or ord(a[0])==45 or (a[0])==43):	
		for i in range(1,f):
			if(ord(a[0])>47 and ord(a[i])<58):
				d=1
			else:
				d=d-1
	else:
		d=d-1
	if(d<0):
		print("invalid Input")
	else:
		if(int(a)<0):
			print("Negative")
		elif((int(a))==0):
			print("Zero")
		else:
			print("Positive")
