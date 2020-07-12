'''
Problem Statement:

Given the array nums, for each nums[i] find out how many numbers in the array are smaller than it. That is, for each nums[i] you have to count the number of valid j's such that j != i and nums[j] < nums[i].

Return the answer in an array.

Example 1:

Input: nums = [8,1,2,2,3]

Output: [4,0,1,1,3]

Explanation: 

For nums[0]=8 there exist four smaller numbers than it (1, 2, 2 and 3). 

For nums[1]=1 does not exist any smaller number than it.

For nums[2]=2 there exist one smaller number than it (1). 

For nums[3]=2 there exist one smaller number than it (1). 

For nums[4]=3 there exist three smaller numbers than it (1, 2 and 2).

Example 2:

Input: nums = [6,5,4,8]

Output: [2,1,0,3]

Example 3:

Input: nums = [7,7,7,7]

Output: [0,0,0,0]

Constraints:

2 <= nums.length <= 500

0 <= nums[i] <= 100

Solution Time Complexity O(n)
Space Complexity O(1)
'''


class Solution:
    def smallerNumbersThanCurrent(self, nums):
        count=[0]*100
        for val in nums:
            count[val]=count[val]+1
        for i in range (1,100):
            count[i]+=count[i-1]
        result=[0]*len(nums)
        for i,val in enumerate(nums):
            if val>0:
                result[i]=count[val-1]
        return result

s=Solution()
print(s.smallerNumbersThanCurrent([8,1,2,2,3])) 