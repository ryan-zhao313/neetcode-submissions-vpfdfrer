class Solution:
    def rob(self, nums: List[int]) -> int:
        # keep track of dp[i-2] and dp[i-1]
        prev2 = 0
        prev1 = nums[0]

        # two choices to rob or to not rob
        # if rob, you have to skip the next house
        for i in range(1, len(nums)):
            current = max(prev1, prev2 + nums[i])
            prev2 = prev1
            prev1 = current

        return prev1

