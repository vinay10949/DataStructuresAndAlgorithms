'''

Problem Statement:

We have some permutation A of [0, 1, ..., N - 1], where N is the length of A.

The number of (global) inversions is the number of i < j with 0 <= i < j < N and A[i] > A[j].

The number of local inversions is the number of i with 0 <= i < N and A[i] > A[i+1].

Return true if and only if the number of global inversions is equal to the number of local inversions.


Example 1:




Input: A = [1,0,2]

Output: true

Explanation: There is 1 global inversion, and 1 local inversion.



Example 2:




Input: A = [1,2,0]

Output: false
'''
def merge(arr,temp,start,end):
    inv_count=0
    if start < end:
        
        mid=(start+end)//2
        
        inv_count+=merge(arr,temp,start,mid)
        
        inv_count+=merge(arr,temp,mid+1,end)
        
        inv_count+=mergeAndCount(arr,temp,start,mid,end)
        
    return inv_count

def mergeAndCount(arr,temp,start,mid,end):
    
    i=start
    j=mid+1
    k=start
    
    inv_count=0
    while i<=mid and j<=end:
        
        if(arr[i] > arr[j]):
            temp[k] = arr[j] 
            inv_count += (mid-i + 1) 
            k += 1
            j += 1
        else:
            temp[k] = arr[i] 
            k += 1
            i += 1
    
    while i<=mid:
        temp[k] = arr[i] 
        k += 1
        i += 1
    
    while j<=end:
        temp[k] = arr[j] 
        k += 1
        j += 1
    
    for i in range(start,end+1):
        arr[i]=temp[i]
        
    return inv_count

if __name__=='__main__':
    arr = [1, 2, 6, 4, 5] 
    n = len(arr) 
    temp=[None]*10
    count=merge(arr,temp,0,n-1)
    print(count)
