class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        res = iter(t)
        return all(i in res for i in s)
                
        
        