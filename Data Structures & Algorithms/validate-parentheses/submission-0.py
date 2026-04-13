class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for i in s:
            if i in "({[":
                stack.append(i)
            else:
                if not stack:
                    return False
                j = stack.pop()
                if (j == "(" and i != ")") or (j == "{" and i != "}") or (j == "[" and i != "]"):
                    return False

        return True if not stack else False