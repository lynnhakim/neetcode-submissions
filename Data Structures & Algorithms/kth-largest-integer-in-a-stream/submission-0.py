class KthLargest:
    """
    [k, [3,[ 1, 4, 3, 3]], add 2]
    [4, 3, 3, 1]
    [2 3 3]
    [ 6 7 8]

    """

    def __init__(self, k: int, nums: List[int]):
        self.heap = nums
        heapq.heapify(self.heap)
        self.k = k
        while len(self.heap) > k:
            heapq.heappop(self.heap)
    

    def add(self, val: int) -> int:
        heapq.heappush(self.heap, val)
        if len(self.heap) > self.k:
            heapq.heappop(self.heap) 

        return self.heap[0]
        
        
