class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        """
        nums = [2,1,3,5,6], k = 5, multiplier = 2
        heap = [(1, 1),(2, 0), (3, 2), (5, 3), (6, 4)]


        """
        res = nums[:]
        min_heap = [(num, i) for i, num in enumerate(nums)]
        heapq.heapify(min_heap)
        for _ in range(k):
            num, i = heapq.heappop(min_heap)
            res[i] *= multiplier
            heapq.heappush(min_heap, (res[i], i))

        return res
