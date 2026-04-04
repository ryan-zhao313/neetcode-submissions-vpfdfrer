class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []

        # Helper function to check palindrome
        def is_palindrome(s):
            return s == s[::-1]

        def backtrack(start, path):
            # Stopping condition where we finished partitioning
            if start == len(s):
                res.append(path[:])
                return
            
            for i in range(start, len(s)):
                if is_palindrome(s[start:i+1]):
                    path.append(s[start:i+1])
                    backtrack(i + 1, path)
                    path.pop()

        backtrack(0, [])
        return res