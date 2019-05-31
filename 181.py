a,b=list(map(int,input().split()))  
for i in range(a,b):  
   sum1i=0  
   temp=i 
   while temp > 0:  
       d=temp%10  
       sum1i+=d**3  
       temp//=10  
       if i==sum1i:  
            print(i,end=' ')  
© 2019 GitHub, Inc.
