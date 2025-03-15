class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        # return true if ransomNote can be constructed by using the letters from magazine and false otherwise.
        for i in ransomNote:
            if i in magazine:
                magazine = magazine.replace(i, "", 1)  
            else:
                return False  
        return True

        