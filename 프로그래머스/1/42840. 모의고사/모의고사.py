def solution(answers):
    first = [1,2,3,4,5]
    second = [2,1,2,3,2,4,2,5]
    third = [3,3,1,1,2,2,4,4,5,5]
    score = [0,0,0]
    answer=[]
    for i, a in enumerate(answers):
        if a == first[i%len(first)]:
            score[0] += 1
        if a == second[i%len(second)]:
            score[1] += 1 
        if a == third[i%len(third)]:
            score[2] += 1
    for i in range(len(score)):
        if score[i] == max(score):
            answer.append(i+1)
    return answer