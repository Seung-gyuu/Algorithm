def solution(s):
    result = ""
    for i , word in enumerate(s.split(" ")):
        for j in range(len(word)):
            result += word[j].upper() if j % 2 == 0 else word[j].lower()
        result += " "
    return result[:-1]