class Solution:
    def digitCount(self, num: str) -> bool:
        n = len(num)
        # index랑 num에 있는 index의 갯수가 같으면 true
        # 다르면 false
        # dict에 넣어서 count로 갯수확인해서 맞는지 조건문걸면?
        count = {}
        for i in num:
            count[i] = count.get(i,0) + 1
            # print(count) #{'1': 2, '2': 1, '0': 1}
        for i in range(n):
            # print(i)
            expected = int(num[i])
            actual = count.get(str(i), 0) 
            if actual != expected:
                return False
        return True