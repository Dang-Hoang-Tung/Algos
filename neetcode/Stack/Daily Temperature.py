class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        stack: list[int] = []
        result = [0] * len(temperatures)

        for idx, temp in enumerate(temperatures):
            while len(stack) and temp > temperatures[stack[-1]]:
                prev_idx = stack.pop()
                distance = idx - prev_idx
                result[prev_idx] = distance
            stack.append(idx)
        
        return result
