class Solution:
    def addBinary(self, a: str, b: str) -> str:
        #0+0 = 0 0+1= 1
        #1+ 1 =0 (10)
        res= []
        c = 0

        #make them the same length
        a, b = a.zfill(max(len(a), len(b))), b.zfill(max(len(a), len(b)))

        for i in range(len(a)-1, -1,-1):
            val = int(a[i]) + int(b[i]) + c
            if val == 0 :
                res.append("0")
                c = 0
            elif val == 1:
                res.append("1")
                c= 0
            elif val == 2:
                res.append("0")
                c = 1
            else:
                res.append("1")
                c = 1
        if c:
            res.append("1")

        return "".join(res[::-1])

        