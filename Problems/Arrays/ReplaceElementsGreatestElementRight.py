'''
Problem Statement:

Given an array arr, replace every element in that array with the greatest element among the elements to its right, and replace the last element with -1.

After doing so, return the array.

Example 1:

Input: arr = [17,18,5,4,6,1]

Output: [18,6,6,6,1,-1]

Constraints:


    1 <= arr.length <= 10^4

    1 <= arr[i] <= 10^5

TimeComplexity= O(n)
SpaceComplexity O(1)    
'''


class Solution(object):
    def replaceElements(self,nums):
        n=len(nums)
        max_ele_seen_so_far=nums[n-1]
        nums[n-1]=-1
        for i in range(n-2,-1,-1):
            temp=nums[i]
            nums[i]=max_ele_seen_so_far
            if temp>max_ele_seen_so_far:
                max_ele_seen_so_far=temp
        return nums

s=Solution()
print(s.replaceElements( [17,18,5,4,6,1]))        