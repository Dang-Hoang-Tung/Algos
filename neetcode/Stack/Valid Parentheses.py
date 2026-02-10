from typing import Mapping

class Solution:
    def isValid(self, s: str) -> bool:
        matching: Mapping[str, str] = {
            ')': '(',
            '}': '{',
            ']': '['
        }

        stack: list[str] = []
        for char in s:
            # opening bracket
            if char in matching.values():
                stack.append(char)
                continue
            # closing bracket
            if len(stack) == 0 or stack[-1] != matching[char]:
                return False
            else:
                stack.pop()
        
        return len(stack) == 0
