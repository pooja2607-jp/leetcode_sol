class Solution:
    def stoneGameVIII(self, stones: list[int]) -> int:
        n = len(stones)
        
        # Calculate prefix sums
        prefix = [0] * n
        prefix[0] = stones[0]
        for i in range(1, n):
            prefix[i] = prefix[i - 1] + stones[i]
            
        # Base case: forces picking up to the last index (n - 1)
        dp = prefix[n - 1]
        
        # Iterate backwards from n - 2 down to index 1
        for i in range(n - 2, 0, -1):
            dp = max(dp, prefix[i] - dp)
            
        return dp