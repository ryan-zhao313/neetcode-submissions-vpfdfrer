class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []

        # check if is palindrome
        def isPalindrome(s):
            return s == s[::-1]

        def backtrack(start, path):
            # stopping condition
            if start == len(s):
                res.append(path[:])
                return

            for i in range(start, len(s)):
                if isPalindrome(s[start:i + 1]):
                    path.append(s[start:i + 1])
                    backtrack(i + 1, path)
                    path.pop()

        backtrack(0, [])
        return res