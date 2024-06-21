def solution(num):
    #can make 1 by repeating 
    count = 0
    while num > 1:
        num = num // 2 if num % 2 == 0 else num * 3 + 1
        count = count + 1
        if count >= 500:
            return -1
    return count 