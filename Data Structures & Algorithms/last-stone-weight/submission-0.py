class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        """
        [1 3 2 4 3 5] 
        [1 2 3 3 4 5]
        pop 5 pop 4
        [1 2 3 3]
        5 - 4 = 1 push 1
        [1 1 2 3 3]
        pop 3 pop 3
        3 - 3 = 0 dont push 
        [1 1 2]
        pop 2 pop 1
        2 - 1 = 1 push 1
        [1]



        []

        
        """
        heap = [-stone for stone in stones]
        heapq.heapify(heap)
        while len(heap) > 1:
            x, y = -heapq.heappop(heap),  -heapq.heappop(heap)
            if abs(x - y) > 0:
                heapq.heappush(heap, -abs(x - y))
            
        return -heap[0] if heap else 0
        
