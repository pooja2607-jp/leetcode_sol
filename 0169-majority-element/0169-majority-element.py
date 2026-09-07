from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        s=Counter(nums)
        n=len(nums)
        for i in s:
            if s[i]>n/2:
                return i