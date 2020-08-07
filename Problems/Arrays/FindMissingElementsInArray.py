'''
Time Complexity O(n)
Space Complexity O(1)
'''
def findMissingConsecutive(arr,n):
    xor=arr[0]
    for i in range(1,n):
        xor^=arr[i]
    for i in range(1,n+3):
        xor^=i
    
    set_no=(xor) & ~(xor-1)

    x=0
    y=0
    for i in range(n):
        if arr[i] & set_no:
            x^=arr[i]
        else:
            y^=arr[i]
    for i in range(1,n+3):
        if i & set_no:
            x^=i
        else:
            y^=i
    return x,y

if __name__=='__main__':
    arr=[2,3,5,6]
    
    x,y=findMissingConsecutive(arr,len(arr))
    
    print(x,y)
            
