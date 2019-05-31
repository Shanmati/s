numi = int(input(""))
sum = 0
temp = numi

while temp > 0:
    digit = temp % 10
    sum += digit ** 3
    temp //= 10
if numi == sum:
    print("yes")
else:
    print("no")
