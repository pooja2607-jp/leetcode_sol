class Solution:
    def lexicographicallySmallestArray(self, nums, limit):
        n = len(nums)

        # Sort values while keeping their original indices
        arr = sorted((value, index) for index, value in enumerate(nums))

        ans = nums[:]

        i = 0

        while i < n:
            j = i

            # Find all values belonging to the same connected group
            while j + 1 < n and arr[j + 1][0] - arr[j][0] <= limit:
                j += 1

            # Original indices of this group
            indices = sorted(arr[k][1] for k in range(i, j + 1))

            # Values are already sorted
            values = [arr[k][0] for k in range(i, j + 1)]

            # Place smallest values at smallest indices
            for index, value in zip(indices, values):
                ans[index] = value

            i = j + 1

        return ans