from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [1] * n

        # Step 1: Left products
        left = 1
        for i in range(n):
            res[i] = left
            left *= nums[i]

        # Step 2: Right products
        right = 1
        for i in range(n - 1, -1, -1):
            res[i] *= right
            right *= nums[i]

        return res