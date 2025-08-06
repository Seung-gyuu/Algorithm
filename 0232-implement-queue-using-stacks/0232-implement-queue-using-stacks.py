class MyQueue(object):

    def __init__(self):
        self.myQ = []


    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.myQ.append(x)

        

    def pop(self):
        """
        :rtype: int
        """
        return self.myQ.pop(0)

    def peek(self):
        """
        :rtype: int
        """
        return self.myQ[0]
        

    def empty(self):
        """
        :rtype: bool
        """
        return len(self.myQ) == 0



# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()