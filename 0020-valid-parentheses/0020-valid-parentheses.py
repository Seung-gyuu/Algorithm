class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False  

        while len(s) !=0:
            if "()" in s:
                s = s.replace("()", "")
            elif "{}" in s:
                s = s.replace("{}", "")
            elif "[]" in s:
                s = s.replace("[]", "")
            else:
                return False
        
        if len(s) == 0:
            return True
            
            
                

        