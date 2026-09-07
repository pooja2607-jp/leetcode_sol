from collections import Counter
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        s=Counter(nums)
        n=len(nums)
        for i in s:
            if s[i]>1:
                return True
        return False
                