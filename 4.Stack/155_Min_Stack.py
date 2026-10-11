class MinStack:

    def __init__(self):
        self.stack = []
        self.ministack = []

    def push(self, value: int) -> None:
        self.stack.append(value)
        if self.ministack != [] and value > self.ministack[-1]:
            self.ministack.append(self.ministack[-1])
        else:
            self.ministack.append(value)
        

    def pop(self) -> None:
        self.stack.pop()
        self.ministack.pop()
        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.ministack[-1]