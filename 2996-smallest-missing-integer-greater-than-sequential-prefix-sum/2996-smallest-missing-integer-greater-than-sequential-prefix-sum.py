class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        total = nums[0]
        i = 1
        while i < len(nums) and nums[i] == nums[i - 1] + 1:
            total += nums[i]
            i += 1
        s = set(nums)
        while total in s:
            total += 1
        return total