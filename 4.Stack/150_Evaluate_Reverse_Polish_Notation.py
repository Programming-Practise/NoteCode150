import operator

class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        op_map = {
            '+': operator.add,
            '-': operator.sub,
            '*': operator.mul,
            '/': operator.truediv,
        }

        stack = []

        for token in tokens:
            if token in op_map:
                a = stack.pop()
                b = stack.pop()
                result = int(op_map[token](b, a))
                stack.append(result)
            else:
                stack.append(int(token))

        return stack[-1]