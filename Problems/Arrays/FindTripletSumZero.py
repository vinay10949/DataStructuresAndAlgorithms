'''
Problem Statement:
Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.



Note:



The solution set must not contain duplicate triplets.



Example:





Given array nums = [-1, 0, 1, 2, -1, -4],



A solution set is:

[

  [-1, 0, 1],

  [-1, -1, 2]

]


'''


class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        n = len(nums)
        result = []
        for i in range(n-1):
            l = i + 1
            r = n-1
            while l < r:
                curr_sum = nums[i] + nums[l] + nums[r]
                if curr_sum == 0:
                    result.append([nums[i], nums[l], nums[r]])
                    l += 1
                    r -= 1
                elif curr_sum < 0:
                    l+=1
                else:
                    r -= 1
        return set([tuple(x) for x in result])


s=Solution()
print(s.threeSum( [-1, 0, 1, 2, -1, -4]))
