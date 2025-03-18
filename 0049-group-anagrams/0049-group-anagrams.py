class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Given an array of strings strs, group the anagrams together.
        group = {} 
        for i in strs:
            word = "".join(sorted(i))

            if word in group:
                group[word].append(i)
            else:
                group[word] = [i]
        
        return list(group.values())
        