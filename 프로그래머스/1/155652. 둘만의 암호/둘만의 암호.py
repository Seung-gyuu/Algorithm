def solution(s, skip, index):
    alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    for l in skip:
        alpha.remove(l)
    
    answer = ''
    for i in s:
        new_letter = alpha[(alpha.index(i) + index) % len(alpha)]
        answer += new_letter
    return answer

