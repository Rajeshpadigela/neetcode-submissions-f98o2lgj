from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        c = sorted(set(nums))   # ✅ fix

        longest = 1
        current = 1

        for i in range(1, len(c)):
            if c[i] == c[i-1] + 1:   # ✅ only compare neighbors
                current += 1
            else:
                longest = max(longest, current)
                current = 1

        return max(longest, current)