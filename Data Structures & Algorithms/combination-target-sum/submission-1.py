class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def backtrack(start, cur_sum, path):
            # stopping condition
            if cur_sum == target:
                res.append(path[:])
                return
            elif cur_sum > target:
                return

            for i in range(start, len(nums)):
                path.append(nums[i])
                backtrack(i, cur_sum + nums[i], path)
                path.pop()

        backtrack(0, 0, [])
        return res