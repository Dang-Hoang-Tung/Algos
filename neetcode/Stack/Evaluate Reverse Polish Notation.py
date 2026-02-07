class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        stack = []
        funcs = {
            '+': (lambda a, b: a + b),
            '-': (lambda a, b: a - b),
            '*': (lambda a, b: a * b),
            '/': (lambda a, b: int(a / b)),
        }
        for token in tokens:
            if token in "+-*/":
                a = stack.pop()
                b = stack.pop()
                stack.append(funcs[token](b, a))
            else:
                stack.append(int(token))
        return stack[0]
