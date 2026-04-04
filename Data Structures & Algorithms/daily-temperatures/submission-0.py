class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        res = [0] * n
        stack = []
        
        for i, t in enumerate(temperatures):
            while stack and stack[-1][0] < t:
                temp, index = stack.pop()
                res[index] = i - index
            
            stack.append((t, i))

        return res

            