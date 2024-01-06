class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = ""
        first = min(strs)
        last = max(strs)
        for i in range(min(len(first), len(last))):
            if first[i] == last[i]:
                prefix += first[i]
            else:
                break
        return prefix

        
       