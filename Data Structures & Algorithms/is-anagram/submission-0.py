class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        v=sorted(list(s))
        w=sorted(list(t))
        if v==w:
            return True
        else:
            return False
        