'''
Problem Statement:
Given an array nums of n integers where n > 1,  return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].



Example:





Input:  [1,2,3,4]

Output: [24,12,8,6]



Constraint: It's guaranteed that the product of the elements of any prefix or suffix of the array (including the whole array) fits in a 32 bit integer.



Note: Please solve it without division and in O(n).



Follow up:

Could you solve it with constant space complexity? (The output array does not count as extra space for the purpose of space complexity analysis.)
'''


def arrayProduct(arr,n):
    output=[0]*n
    left=1
    right=1
    for i in range(n):
        output[i]=left
        left*=arr[i]
    print("Output ",output)    
    for i in range(n-1,-1,-1):
        output[i]*=right
        right*=arr[i]
    print(output)

if __name__=='__main__':
    arr=[10, 3, 5, 6, 2]
    arrayProduct(arr,len(arr))
