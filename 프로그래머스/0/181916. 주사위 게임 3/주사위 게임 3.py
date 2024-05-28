def solution(a, b, c, d):
    answer = 0
    nums = [a,b,c,d]
    uniq_num = list(set([a,b,c,d]))
    #1)all same number in 4 dices -> 1111 x p
    if a == b == c == d == a:
        return 1111 * a
    #all different -> the smallest number
    elif len(uniq_num) == 4: 
        return min(uniq_num)
    else:    
        for i, var in enumerate(uniq_num):
            #4) 2 same number, 2 different number in 4 dices ->  q × r
            if len(uniq_num) == 3:
                if nums.count(var) == 2:
                    uniq_num.remove(var)
                    return uniq_num[0] * uniq_num[1]
            #2)3 same number in 4 dices -> (10 × p + q)2
            elif nums.count(var) == 3: 
                q = [x for x in uniq_num if x != var][0]
                return pow((10 * var + q),2)
            #3) each 2 same number in 4 dices -> (p + q) × |p - q|
            elif nums.count(var) == 2:
                return (uniq_num[0] + uniq_num[1]) * abs(uniq_num[0] - uniq_num[1])

