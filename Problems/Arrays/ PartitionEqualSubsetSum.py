'''
Problem Statement:
Given a non-empty array containing only positive integers, find if the array can be partitioned into two subsets such that the sum of elements in both subsets is equal.



Note:




Each of the array element will not exceed 100.

The array size will not exceed 200.



Example 1:

Input: [1, 5, 11, 5]

Output: true

Explanation: The array can be partitioned as [1, 5, 5] and [11].

Example 2:

Input: [1, 2, 3, 5]

Output: false

Explanation: The array cannot be partitioned into equal sum subsets.

Time Complexity : O(n)
Space Complexity: O(n)
'''



def getSplitpoint(arr,n):
    leftsum=0
    rightsum=0
    for i in range(n):
        leftsum+=arr[i]
    
    for i in range(n-1,-1,-1):
        rightsum+=arr[i]
        leftsum-=arr[i]
        if leftsum==rightsum:
            return i
    return -1

if __name__=='__main__':
    arr=[1,2,3,4,5,5]
    point=getSplitpoint(arr,len(arr))
    if(point==-1 or point==len(arr)):
        print("Split cannot be done")
    else:
        for i in range(len(arr)):
            if i==point:
                print("\n")
            print(arr[i]),
