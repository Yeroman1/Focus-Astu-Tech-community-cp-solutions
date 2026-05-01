class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        p = 0
        mp = 0
        max_sum = float('-inf')

        for num in nums:
            p += num
            max_sum = max(max_sum, p - mp)
            mp = min(mp, p)

        return max_sum
