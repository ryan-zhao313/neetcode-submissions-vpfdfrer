class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [0] * n

        prefixProduct = [1] * n
        suffixProduct = [1] * n

        for i in range(1, n):
            prefixProduct[i] = nums[i-1] * prefixProduct[i-1]

        for i in range(n-2, -1, -1):
            suffixProduct[i] = nums[i+1] * suffixProduct[i+1]

        for i in range(n):
            res[i] = prefixProduct[i] * suffixProduct[i]
        
        return res