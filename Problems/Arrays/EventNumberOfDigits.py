'''
Problem Statement:

Given an array nums of integers, return how many of them contain an even number of digits.

Example 1:


Input: nums = [12,345,2,6,7896]

Output: 2

Explanation: 

12 contains 2 digits (even number of digits). 

345 contains 3 digits (odd number of digits). 

2 contains 1 digit (odd number of digits). 

6 contains 1 digit (odd number of digits). 

7896 contains 4 digits (even number of digits). 

Therefore only 12 and 7896 contain an even number of digits.



Example 2:





Input: nums = [555,901,482,1771]

Output: 1 

Explanation: 

Only 1771 contains an even number of digits.

Constraints:



1 <= nums.length <= 500

1 <= nums[i] <= 10^5
'''
import math
class Solution:
    def findNumbers(self, nums):
        num_even = 0
        for num in nums:
            log_val = math.log10(num)
            num_digits = int(math.floor(log_val)) + 1
            if num_digits % 2 == 0:
                num_even += 1
        return num_even


s=Solution()
print(s.findNumbers([1,23,4,567,2435]))
