class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pair = {"(" : ")", "{": "}", "[":"]"}

        for i in s:
            print(i)
            if i in "({[":
                stack.append(i)
            else:
                if not stack or pair[stack[-1]] != i:
                    return False
                stack.pop()
        return len(stack) == 0



        