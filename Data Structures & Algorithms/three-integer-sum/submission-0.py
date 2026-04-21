class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = set()

        # sort the list
        nums.sort()
        n = len(nums)

        for i in range(n):
            for j in range(i + 1, n):
                curr = nums[i] + nums[j]
                k = j + 1
                while k < n:
                    if curr + nums[k] == 0:
                        res.add((nums[i], nums[j], nums[k]))
                    
                    elif curr + nums[k] > 0:
                        break
                    k += 1

        return list(res)