def solution(k, score):
    #create lists to track the highest score and the lowest one in the program
    highest,lowest = [], []
    #if the num of score is greater than k
    if k < len(score):
        for i in range(k):
            highest.append(score[i])
            lowest.append(min(highest)) 
    else:
        for i in range(len(score)):
            highest.append(score[i])
            lowest.append(min(highest)) 

    for idx in range(len(score[k:])):
            # sort the list        
        highest = sorted(highest)  
        #if the current is greater than the lowest in the 'highest' list
        if score[k + idx] > highest[0]:
            #replace the lowest score
            highest[0] = score[k + idx]
        lowest.append(min(highest)) 
    return lowest