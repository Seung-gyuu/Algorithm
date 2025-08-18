class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        # 한번 이상 나오는 substring찾기
        #sliding window
        n = len(s)
        k = 10
        seen = set()
        res = set()

        if n < 10:
            return []


        for i in range(n):
            seq = s[i:i+k]
            if seq in seen:
                res.add(seq)
            else:
                seen.add(seq)
        return list(res)

        