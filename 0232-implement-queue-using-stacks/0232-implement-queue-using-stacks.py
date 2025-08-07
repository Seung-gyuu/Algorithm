class MyQueue(object):

    def __init__(self):
        self.stack_in = []
        self.stack_out = []

    def push(self, x: int) -> None:
        self.stack_in.append(x)

    def pop(self) -> int:
        while self.stack_in:
            self.stack_out.append(self.stack_in.pop())
        front_value = self.stack_out.pop()
        while self.stack_out:
            self.stack_in.append(self.stack_out.pop())
        return front_value

    def peek(self) -> int:
        return self.stack_in[0]

    def empty(self) -> bool:
        return len(self.stack_in) == 0

# 질문을 제대로 이해를 하지 않고 그냥 큐만 사용함
        # 정리
# 큐(First-In-First-Out) 자료구조를 스택(Last-In-First-Out) 두 개만으로 구현하는 문제
# LIFO 구조 2개를 조합해서 어떻게 FIFO처럼 보이게 만들 수 있을까?
# 두 개의 스택으로 방향을 뒤집는 아이디어
# 최소한의 이동으로 pop/peek 처리 → 시간 최적화 포인트

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
