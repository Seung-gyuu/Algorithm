class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # find the longest substring 
        left, max_len = 0, 0
        seen = set()
        for right in range(len(s)):
            # right moves to expand the window
            # left only moves if the window becomes invalid (e.g., when a duplicate character appears)
            while s[right] in seen:
                seen.remove(s[left])
                left += 1
            seen.add(s[right])
            max_len = max(max_len, right - left + 1)
        return max_len

        