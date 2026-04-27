class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        hashs = {}
        hasht = {}

        for c in s:
            hashs[c] = hashs.get(c,0) + 1
        for c in t:
            hasht[c] = hasht.get(c,0) + 1
        
        for c in s:
            if hashs.get(c) != hasht.get(c):
                return False
        
        return True

        
    