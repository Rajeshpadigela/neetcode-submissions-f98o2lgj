class Solution:
    def threeSum(self, nums):
        res = []
        nums.sort()
        
        for i, a in enumerate(nums):
            if i > 0 and a == nums[i - 1]:
                continue
            
            l, r = i + 1, len(nums) - 1  # ✅ correct indentation
            
            while l < r:
                tsum = a + nums[l] + nums[r]
                
                if tsum > 0:
                    r -= 1
                elif tsum < 0:
                    l += 1
                else:
                    res.append([a, nums[l], nums[r]])
                    
                    l += 1
                    r -= 1
                    
                    # ✅ skip duplicates (left)
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                    
                    # ✅ skip duplicates (right)
                    while l < r and nums[r] == nums[r + 1]:
                        r -= 1
        
        return res