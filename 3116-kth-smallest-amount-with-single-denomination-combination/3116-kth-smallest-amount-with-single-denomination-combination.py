import math
from typing import List

class Solution:
    def findKthSmallest(self, coins: List[str], k: int) -> int:
        n = len(coins)
        
        # Helper function to count valid amounts <= x using Inclusion-Exclusion
        def count_valid(x: int) -> int:
            total = 0
            # Iterate through all non-empty subsets of coins
            for i in range(1, 1 << n):
                lcm_val = 1
                bits_set = 0
                for j in range(n):
                    if (i >> j) & 1:
                        bits_set += 1
                        lcm_val = (lcm_val * coins[j]) // math.gcd(lcm_val, coins[j])
                        # If LCM exceeds x, this subset adds 0 to the count
                        if lcm_val > x:
                            break
                
                if lcm_val <= x:
                    # Odd size subsets are added, even size subsets are subtracted
                    if bits_set % 2 == 1:
                        total += x // lcm_val
                    else:
                        total -= x // lcm_val
                        
            return total

        # Binary search bounds
        min_coin = min(coins)
        low = min_coin
        high = min_coin * k
        ans = high
        
        while low <= high:
            mid = (low + high) // 2
            if count_valid(mid) >= k:
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
                
        return ans