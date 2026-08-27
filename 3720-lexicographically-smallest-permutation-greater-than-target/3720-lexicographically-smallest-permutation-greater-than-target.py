from collections import Counter

class Solution:
    def lexGreaterPermutation(self, s: str, target: str) -> str:
        n = len(s)
        s_counts = Counter(s)
        
        # Try to match a prefix of length i (from n-1 down to 0)
        for i in range(n - 1, -1, -1):
            # Count character frequencies required for target[0...i-1]
            prefix_counts = Counter(target[:i])
            
            # Check if target[0...i-1] can be formed using available characters in s
            if any(prefix_counts[ch] > s_counts[ch] for ch in prefix_counts):
                continue
            
            # Remaining characters available after forming target[0...i-1]
            rem_counts = s_counts - prefix_counts
            
            # Find the smallest available character strictly greater than target[i]
            target_char = target[i]
            for c in sorted(rem_counts.keys()):
                if c > target_char and rem_counts[c] > 0:
                    rem_counts[c] -= 1
                    
                    # Sort remaining characters to form the smallest valid suffix
                    suffix = "".join(char * rem_counts[char] for char in sorted(rem_counts.keys()))
                    
                    return target[:i] + c + suffix
                    
        return ""