class Solution:
    def minimumDeletions(self, nums: list[int]) -> int:
        n = len(nums)
        if n <= 2:
            return n
            
        # Find the indices of the minimum and maximum elements
        min_idx = nums.index(min(nums))
        max_idx = nums.index(max(nums))
        
        # Ensure i is the smaller index and j is the larger index
        i = min(min_idx, max_idx)
        j = max(min_idx, max_idx)
        
        # Strategy 1: Delete both from the front
        del_front = j + 1
        
        # Strategy 2: Delete both from the back
        del_back = n - i
        
        # Strategy 3: Delete one from front, one from back
        del_both = (i + 1) + (n - j)
        
        return min(del_front, del_back, del_both)
