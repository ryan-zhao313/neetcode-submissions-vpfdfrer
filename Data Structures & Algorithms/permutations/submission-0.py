class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)
        visited = [False] * n

        # skip if the integer is the same
        def backtrack(path, visited):
            # stopping condition if the length is equal to the length of nums
            if len(path) == n:
                res.append(path[:])
                return
            
            for i in range(n):
                if not visited[i]:
                    visited[i] = True
                    path.append(nums[i])
                    backtrack(path, visited)
                    path.pop()
                    visited[i] = False

        backtrack([], visited)
        return res