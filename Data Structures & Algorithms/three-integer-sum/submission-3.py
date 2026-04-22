class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        n = len(nums)

        for i in range(n):
            if nums[i] > 0:
                break
            
            # skip duplicate numbers
            if i > 0 and nums[i] == nums[i-1]:
                continue

            j, k = i + 1, n - 1
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
                    # skip duplicates for j
                    while nums[j] == nums[j-1] and j < k:
                        j += 1
        return res