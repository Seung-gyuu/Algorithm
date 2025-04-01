class Solution(object):
    def hammingWeight(self, n):
        num = bin(n)[2:]
        return sum(1 for i in num if i == '1')
        