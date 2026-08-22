class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        """
        [0, 2], [0, 4], [1, 2]
        sqrt((x1)^2 + (y1^2) for each subarr
        2^2 = 4
        heap = [4] len< k
        4^2
        [4, 16] len < 3
        2+ 4 = 6
        heap [(4, [0, 2]), 6, 16] len = k=3


        """
        heap = []
        for x, y in points:
            dist = math.sqrt(x**2 + y**2)
            heapq.heappush(heap, (-dist, [x, y]))
            if len(heap) > k:
                heapq.heappop(heap)
        return [c for d, c in heap]

