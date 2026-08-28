from collections import Counter

class Solution:
    def lexPalindromicPermutation(self, s: str, target: str) -> str:
        n = len(s)
        m = n // 2
        
        # Count character frequencies
        counts = Counter(s)
        odd_char = ""
        for char, cnt in counts.items():
            if cnt % 2 == 1:
                if odd_char:
                    return ""  # More than 1 odd frequency char -> impossible
                odd_char = char
                
        # Half-length character counts
        half_counts = {char: cnt // 2 for char, cnt in counts.items()}
        
        def can_form_prefix(prefix):
            req = Counter(prefix)
            # Use .get(c, 0) to avoid KeyError when target contains chars not in s
            return all(half_counts.get(c, 0) >= req[c] for c in req)

        def build_palindrome(left_half):
            return left_half + odd_char + left_half[::-1]

        candidates = []

        # 1. Try exact prefix match for left half
        target_left = target[:m]
        if can_form_prefix(target_left):
            pal = build_palindrome(target_left)
            if pal > target:
                candidates.append(pal)

        # 2. Try diverging at position i (from m-1 down to 0)
        for i in range(m - 1, -1, -1):
            prefix = target_left[:i]
            if not can_form_prefix(prefix):
                continue
            
            used = Counter(prefix)
            avail = {c: half_counts[c] - used.get(c, 0) for c in half_counts}
            
            # Pick smallest character strictly greater than target[i]
            for c in sorted(avail.keys()):
                if c > target_left[i] and avail[c] > 0:
                    avail[c] -= 1
                    remaining = "".join(sorted([char * cnt for char, cnt in avail.items() if cnt > 0]))
                    
                    left_half = prefix + c + remaining
                    candidates.append(build_palindrome(left_half))
                    break  # Smallest 'c' at position i is optimal for this index

        return min(candidates) if candidates else ""