def solution(my_string, index_list):
    answer = ""
    #make index and each element of my_string into one dictionary 
    dicts = {i: v for i, v in enumerate(list(my_string))}
    # create string
    for i in index_list:
        answer += dicts[i]    
    return answer