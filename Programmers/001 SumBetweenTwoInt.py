# Sum between two integers

## Complete the function solution which takes two integers, a and b, and returns the sum of all integers between a and b, inclusive.
## For example, if a = 3 and b = 5, the function should return 12 since 3 + 4 + 5 equals 12.
def solution(a, b):
  # Think about 3 cases i) a = b ii) a > b iii) a < b 
    if a == b:
        return a
    else: 
        answer = 0
        if a > b: 
            for i in range(b, a + 1):          
                answer += i
        else:
             for i in range(a, b + 1):          
                answer += i                
    return answer

# Suggestion:
# Try to use sum, min, and, max function 
def solution(a, b):
    if a == b:
        return a
    else:
        answer = sum(range(min(a, b), max(a,b)+1))
        return answer
