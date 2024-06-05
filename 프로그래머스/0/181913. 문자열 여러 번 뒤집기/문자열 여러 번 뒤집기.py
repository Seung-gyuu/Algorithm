def solution(my_string, queries):
    for query in queries:
        start, end = query
        #using string slicing - reverse indexes
        new = my_string[end::-1] if start == 0 else my_string[end: start-1 :-1]
        my_string = my_string[:start]+ new + my_string[end+1:]
    return my_string