class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        #AND 비트연산: 모든 자리에서 1이 있어야 1. 아니면 0
        shift = 0
        while left < right:
            left >>= 1
            right >>= 1
            shift += 1
        return left << shift

