class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def backtrack(start, cur_sum, path):
            # stopping point to check if sum is equal to the target
            if cur_sum == target:
                res.append(path[:])
                return
            elif cur_sum > target:
                return

            for i in range(start, len(nums)):
                path.append(nums[i])
                cur_sum += nums[i]
                backtrack(start, cur_sum, path)
                start += 1
                path.pop()
                cur_sum -= nums[i]

        backtrack(0, 0, [])
        return res