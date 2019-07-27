def isSubsetSum (arr, n, sum): 


    if sum == 0: 

        return True

    elif n == 0 and sum != 0:
        return False

    elif arr[n-1] > sum: 

        return isSubsetSum (arr, n-1, sum) 


      

    return isSubsetSum (arr, n-1, sum) or isSubsetSum (arr, n-1, sum-arr[n-1]) 

  

def findPart (arr, n): 


    sum = 0

    for i in range(0, n): 

        sum += arr[i] 

    if sum % 2 != 0: 

        return false 

  

    return isSubsetSum (arr, n, sum // 2)
n = int(input())
arr = input()



if findPart(arr, n) == True: 

    print ("yes") 

else: 

    print ("no") 
