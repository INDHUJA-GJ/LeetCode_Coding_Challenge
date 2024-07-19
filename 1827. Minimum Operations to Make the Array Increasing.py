class Solution(object):
    def minOperations(self, nums):
        count=0
        for i in range(0,len(nums)):
            if i+1<len(nums):
                if nums[i+1]<=nums[i]:
                    count=count-nums[i+1]+nums[i]+1
                    nums[i+1]=nums[i]+1

        return count
        
