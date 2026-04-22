class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        res = []

        for i in range(n):
            # stop early
            if nums[i] > 0:
                break
            
            # avoid duplicates
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            j = i + 1
            k = n - 1
            while j < k:
                curr = nums[i] + nums[j] + nums[k]
                if curr < 0:
                    j += 1
                elif curr > 0:
                    k -= 1
                else:
                    res.append([nums[i], nums[j], nums[k]])
                    j += 1
                    k -= 1
                    # skip duplicates
                    while j < k and nums[j] == nums[j-1]:
                        j += 1
        return res