class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {')': '(', '}': '{', ']': '['}

        for i in s:
            if i in mapping:
                if not stack or stack.pop() != mapping[i]:
                    return False
            else:
                stack.append(i)

        return not stack