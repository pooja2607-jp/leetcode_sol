class Solution:
    def maxNumberOfFamilies(self, n, reservedSeats):
        rows = {}

        # Store reserved seats for each affected row
        for row, seat in reservedSeats:
            if row not in rows:
                rows[row] = set()
            rows[row].add(seat)

        ans = 2 * n

        for seats in rows.values():

            # Check left block: 2,3,4,5
            left = all(seat not in seats for seat in [2, 3, 4, 5])

            # Check middle block: 4,5,6,7
            middle = all(seat not in seats for seat in [4, 5, 6, 7])

            # Check right block: 6,7,8,9
            right = all(seat not in seats for seat in [6, 7, 8, 9])

            # This row was initially counted as 2
            if left and right:
                # Still 2 groups, so no change
                continue

            elif left or middle or right:
                # Only 1 group can fit
                ans -= 1

            else:
                # No group can fit
                ans -= 2

        return ans