class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # Use a min heap and keep only 'k' elements inside
        minHeap = []
        for num in nums:
            heapq.heappush(minHeap, num)
            if len(minHeap) > k:
                heapq.heappop(minHeap)
        
        return heapq.heappop(minHeap)