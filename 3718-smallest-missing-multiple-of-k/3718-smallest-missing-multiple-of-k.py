class Solution:
    def missingMultiple(self, nums, k):
        x = k

        while x in nums:
            x += k

        return x