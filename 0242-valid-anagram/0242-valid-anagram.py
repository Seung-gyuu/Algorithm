class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Given two strings s and t, return true if t is an anagram of s, and false otherwise.
        if len(s) != len(t):  
            return False

        res = set(s)

        for i in res:
            if s.count(i) != t.count(i):
                return False
        return True

        