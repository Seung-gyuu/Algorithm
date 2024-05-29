def solution(x1, x2, x3, x4):
    # x = x1 V x2 
    # y = x3 V x4
    x = False if x1 == False and x2 == False else True
    y = False if x3 == False and x4 == False else True
    # x ∧ y
    return True if x == True and y == True else False
