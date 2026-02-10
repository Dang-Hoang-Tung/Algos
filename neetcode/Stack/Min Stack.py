class MinStack:
    stack: list[int]

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        self.stack = self.stack + [val]

    def pop(self) -> None:
        self.stack = self.stack[:-1]

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return min(self.stack)
