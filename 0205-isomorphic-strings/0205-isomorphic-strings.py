class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        # create dict
        s_to_t = {}
        t_to_s = {}

        if len(s) != len(t):
            return False
        # check if s[i] is in t, if so, it is same as t[i]
        for i in range(len(s)):
            s_let = s[i]
            t_let = t[i]

            if s_let in s_to_t and s_to_t[s_let] != t_let: 
                return False
            
            if t_let in t_to_s and t_to_s[t_let] != s_let:
                return False

            s_to_t[s_let] = t_let
            t_to_s[t_let] = s_let
        
        return True

                

        