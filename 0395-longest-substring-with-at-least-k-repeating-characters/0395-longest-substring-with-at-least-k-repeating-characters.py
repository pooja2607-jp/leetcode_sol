from collections import defaultdict

class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        ans = 0

        # Try every possible number of unique characters
        for target_unique in range(1, 27):
            freq = defaultdict(int)
            left = 0
            right = 0

            unique = 0          # Number of unique characters in window
            count_at_least_k = 0  # Number of characters with frequency >= k

            while right < len(s):
                # Expand window
                if freq[s[right]] == 0:
                    unique += 1
                freq[s[right]] += 1

                if freq[s[right]] == k:
                    count_at_least_k += 1

                right += 1

                # Shrink window if unique characters exceed target
                while unique > target_unique:
                    if freq[s[left]] == k:
                        count_at_least_k -= 1

                    freq[s[left]] -= 1

                    if freq[s[left]] == 0:
                        unique -= 1

                    left += 1

                # Update answer
                if unique == count_at_least_k:
                    ans = max(ans, right - left)

        return ans