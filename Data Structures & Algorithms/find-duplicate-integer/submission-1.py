class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        res =0
        for n in nums:
            n=abs(n)
            if nums[n-1]<0:
                res=n
            nums[n-1]=-nums[n-1]
        return res
        