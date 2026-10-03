class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {'}':'{', ']':'[', ')':'('}

        for cha in s:
            if cha in mapping:
                if stack and stack[-1] == mapping[cha]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(cha)
        
        return not stack

