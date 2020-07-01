def findMissingNum(a,n):
    x1 = a[0] 
    x2 = 1
    
    for i in range(1, n): 
        x1 = x1 ^ a[i]      #As mentioned in the video we are doing XOR of the array elements
    for i in range(2, n + 2): 
        x2 = x2 ^ i        #Now we are applying the xor operation on indices 
      
    return x1 ^ x2          # If you apply XOR of the x1 and x2 then you get the missing number
if __name__=='__main__':
    l=[3,4,-1,1]
    n=len(l)
    miss=findMissingNum(l,n)
    print(miss)

