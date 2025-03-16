class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()
        if len(pattern) != len(words):
            return False

        p_to_w = {}
        w_to_p = {}

        for idx, (p, w) in enumerate(zip(pattern, words)):
            if p not in p_to_w:
                p_to_w[p] = w
            elif p in p_to_w and p_to_w[p] != w:
                return False

            if w not in w_to_p:
                w_to_p[w] = p
            elif w in w_to_p and w_to_p[w] != p:
                return False

        return True




