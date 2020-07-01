class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l=len(nums)
        x1=nums[0]
        x2=1
        for i in range(1, l): 
            x1 = x1 ^ nums[i] 
            print(x1)
        return x2
    
s=Solution()
arr=[1,2,0]
print(s.firstMissingPositive(arr))   