import heapq

class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        # Keep a min-heap of size k
        min_heap = []
        
        for num in nums:
            heapq.heappush(min_exp := min_heap, num) # Push current element
            if len(min_heap) > k:
                heapq.heappop(min_heap) # Pop the smallest if size exceeds k
                
        # The root of the min-heap is the kth largest element
        return min_heap[0]