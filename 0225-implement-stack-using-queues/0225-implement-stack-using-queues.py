class MyStack:
    #Q - FIFO
    #S - LIFO

    def __init__(self):
        #객체안에 공유해서 사용해야 하기 때문에 self붙이기
        self.in_queue = []
        self.out_queue = []

        

    def push(self, x: int) -> None:
        self.out_queue.append(x)
        while self.in_queue:
            self.out_queue.append(self.in_queue.pop(0))
        self.out_queue, self.in_queue = self.in_queue, self.out_queue
        
        

    def pop(self) -> int:
        return self.in_queue.pop(0)
        

    def top(self) -> int:
        return self.in_queue[0]
        

    def empty(self) -> bool:
        return len(self.in_queue) == 0

        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()