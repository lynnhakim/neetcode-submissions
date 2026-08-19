class Solution:
    import heapq
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        [2, 1,1, 3,2,2]
        2: 3
        1: 2
        3: 1
        
        """
        freq = {}
        res = []
        for num in nums:
            freq[num] = 1 + freq.get(num, 0)
        
        heap = [(-key, value) for value, key in freq.items()]
        heapq.heapify(heap)
        while k > 0: 
            popped = heapq.heappop(heap)[1]
            res.append(popped)
            k -= 1
        return res


        
