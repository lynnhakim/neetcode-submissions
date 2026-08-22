class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        """
        [1 3 2 5 3 4] k = 3
        [1 2 3 3 4 5]
        [-5 -4 -3 -3 -2 -1]
        heap[3 - 1] = heap[2] = -3 (negate again)



        """
        heap = [-num for num in nums]
        heapq.heapify(heap)
        for i in range(k - 1):
            heapq.heappop(heap)
        return -heapq.heappop(heap)

