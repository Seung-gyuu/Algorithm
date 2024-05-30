def solution(s):
    #count the number of 'p' and 'y'
    num_p = sum(1 for i in s if 'p' == i or 'P' == i)
    num_y = sum(1 for i in s if 'y' == i or 'Y' == i)
    print(num_p, num_y)
    #if same or no p and y, True
    #if not, False
    return True if num_p == num_y else False
