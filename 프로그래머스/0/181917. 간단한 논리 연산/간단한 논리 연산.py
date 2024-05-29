def solution(x1, x2, x3, x4):
    # x = x1 V x2 
    # y = x3 V x4
    x = False if x1 == False and x2 == False else True
    y = False if x3 == False and x4 == False else True
    # x ∧ y
    return True if x == True and y == True else False
    #Another Answer
    return (x1 | x2 ) & (x3 | x4)
    # 1. **OR Operation (\(\mid\))**: This operation means that at least one of the conditions on either side of the OR must be true for the whole expression to be true.
    # - \(x1 \mid x2\) means that either \(x1\) is true, or \(x2\) is true, or both are true.
    # - \(x3 \mid x4\) means that either \(x3\) is true, or \(x4\) is true, or both are true.

    # 2. **AND Operation (\(\&\))**: This operation means that both conditions on either side of the AND must be true for the whole expression to be true. 
    #    - \((x1 \mid x2)\) must be true.
    #    - \((x3 \mid x4)\) must be true.
