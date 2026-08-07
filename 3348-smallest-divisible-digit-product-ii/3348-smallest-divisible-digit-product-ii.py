class Solution:
    def smallestNumber(self, num: str, t: int) -> str:
        # Step 1: Factorize t into powers of 2, 3, 5, 7
        def get_factors(n: int):
            c2 = c3 = c5 = c7 = 0
            while n % 2 == 0:
                c2 += 1
                n //= 2
            while n % 3 == 0:
                c3 += 1
                n //= 3
            while n % 5 == 0:
                c5 += 1
                n //= 5
            while n % 7 == 0:
                c7 += 1
                n //= 7
            if n > 1:
                return None  # t has prime factors other than 2, 3, 5, or 7
            return [c2, c3, c5, c7]

        # Helper to divide factors when selecting a digit d
        def consume(factors, d):
            c2, c3, c5, c7 = factors
            while d % 2 == 0 and c2 > 0:
                c2 -= 1
                d //= 2
            while d % 3 == 0 and c3 > 0:
                c3 -= 1
                d //= 3
            while d % 5 == 0 and c5 > 0:
                c5 -= 1
                d //= 5
            while d % 7 == 0 and c7 > 0:
                c7 -= 1
                d //= 7
            return [c2, c3, c5, c7]

        # Minimum number of digit positions needed to cover remaining target factors
        def min_digits_needed(factors):
            c2, c3, c5, c7 = factors
            # 5s and 7s each need their own digit
            count = c5 + c7
            
            # Combine 3s into 9s and 2s into 8s
            n9 = c3 // 2
            c3 %= 2
            n8 = c2 // 3
            c2 %= 3
            
            if c2 == 2:          # Use digit 4
                count += 1
                c2 = 0
            elif c2 == 1 and c3 == 1:  # Use digit 6
                count += 1
                c2 = c3 = 0
            elif c2 == 1:        # Use digit 2
                count += 1
                c2 = 0
                
            if c3 == 1:          # Use digit 3
                count += 1
                c3 = 0
                
            return count + n9 + n8

        # Greedily constructs the lexicographically smallest suffix of given length
        def fill_suffix(length, factors):
            res = []
            for _ in range(length):
                for d in range(1, 10):
                    next_f = consume(factors, d)
                    if min_digits_needed(next_f) <= length - 1 - len(res):
                        res.append(str(d))
                        factors = next_f
                        break
            return "".join(res)

        # Main logic
        target_f = get_factors(t)
        if target_f is None:
            return "-1"

        n = len(num)

        # Handle '0' in num - prefix can only extend up to the first '0'
        first_zero = num.find('0')
        limit = n if first_zero == -1 else first_zero

        # Store factor state after consuming each character of num's prefix
        prefix_f = [target_f]
        for i in range(limit):
            prefix_f.append(consume(prefix_f[-1], int(num[i])))

        # 1. Try to find a valid string of the SAME length n
        # Check if exact num works (only if no '0' and factors are satisfied)
        if first_zero == -1 and min_digits_needed(prefix_f[n]) == 0:
            return num

        # Try matching prefix up to position i, then picking digit d > num[i]
        for i in range(limit, -1, -1):
            start_digit = int(num[i]) + 1 if i < limit else 1
            for d in range(start_digit, 10):
                next_f = consume(prefix_f[i], d)
                remaining_len = n - 1 - i
                if min_digits_needed(next_f) <= remaining_len:
                    prefix = num[:i] + str(d)
                    suffix = fill_suffix(remaining_len, next_f)
                    return prefix + suffix

        # 2. If no valid candidate of length n exists, construct for length n + 1
        req_len = max(n + 1, min_digits_needed(target_f))
        return fill_suffix(req_len, target_f)