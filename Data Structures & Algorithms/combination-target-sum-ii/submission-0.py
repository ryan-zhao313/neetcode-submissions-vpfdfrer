class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()

        def backtrack(start, cur_sum, path):
            # stopping condition
            if cur_sum == target:
                res.append(path[:])
                return
            elif cur_sum > target:
                return

            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i-1]:
                    continue

                path.append(candidates[i])
                backtrack(i+1, cur_sum + candidates[i], path)
                path.pop()

        backtrack(0, 0, [])
        return res