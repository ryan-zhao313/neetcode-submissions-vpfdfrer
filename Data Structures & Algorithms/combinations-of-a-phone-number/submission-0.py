class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []

        # Map the digits to the letter
        digit_map = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "qprs",
            "8": "tuv",
            "9": "wxyz",
        }

        def backtrack(i, string):
            # stopping condition when length of string is equal to the length of digits
            if i == len(digits):
                res.append(string)
                return
            
            for c in digit_map[digits[i]]:
                backtrack(i + 1, string + c)

        # edge case where there are no digits
        if digits:
            backtrack(0, "")
        return res


            
