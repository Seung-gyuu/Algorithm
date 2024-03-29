# Complete the function solution that returns a string in the form "(minimum value) (maximum value)", where s contains numbers separated by spaces. 
# For example, if s is "1 2 3 4", it should return "1 4", and if s is "-1 -2 -3 -4", it should return "-4 -1".

def solution(s):
    num_list = list(map(int, s.split()))
    min_num = min(num_list)
    max_num = max(num_list)
    answer = f'{min_num} {max_num}'
    return answer

-----------------------------------------------------------------------------------------------------------------------------------------------------
## Need to know 

# 1) string.split(sep, maxsplit): Split a string into a list 

default separator - any whitespace  ex) s.split()
maxsplit(optional) - specifies how many splits to do. default is -1(all occurances)
each element is str

ex) 
s = "This is me Thank you"
result = s.split(" " ,1) 
# result = ['This', 'is me Thank you']

# 2) list(map(function, iterable)): apply the given function to each item of a given list 

Create new list not changing existing list 
Commonly used with list and tuple
ex1)If you want to change datatype of each element of the list: list(map(int, list_name))

+)map(function, iterable1, iterable2, ...): can be used with multiple iterables
ex2)
def multiply(a,b):
	return a * b
 
list_a = [3,6,1,8,19]
list_b = [57,7,9,10]
result = list(map(multiply, list_a, list_b))
