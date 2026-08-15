class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left=0
        sum=0
        ans=float('inf')
        for right in range(len(nums)):
            sum+=nums[right]
            while sum>=target:
                ans=min(ans,right-left+1)
                sum-=nums[left]
                left+=1
        if ans==float('inf'):
            return 0
        return ans

