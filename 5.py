za=input()
za=za.split(" ")
if(int(za[0])>int(za[1]) and int(za[1])> int(za[2])):
  c=za[0]
elif(int(za[1])>int(za[0]) and int(za[1])>int(za[2])):
  c=za[1]
else:
  c=za[2]
print(c)
