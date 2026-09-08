class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:

        freq = {}
        result = []

        for x in nums2:
            freq[x] = freq.get(x, 0) + 1

        for i in range(len(nums1)):
            if freq.get(nums1[i], 0) > 0:
                result.append(nums1[i])
                freq[nums1[i]] -= 1

        return result