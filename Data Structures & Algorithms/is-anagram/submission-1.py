class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        a=list(s)
        b=list(t)
        print("a:", a , "b:", b)
        
        return sorted(a) == sorted(b)