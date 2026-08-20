class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        """
        {6}
        1 4 3 2 h = 9
        sort: 1 2 3 4 -> 
        lo: 1 ; hi 4 -> mid = (4 + 1) //2 = 2

        for loop : while >0
            1/2 = 0.5-> 1
            2/2 =1
            3/2 = 2
            4/ 2 = 2
            1 - 2 <= 0: count += 1
            2 - 2 <= 0: count += 1
            3 - 2 = 1: count += 1
            1 - 2 <=0: count += 1
            4- 2 count += 1
            2 -2 = 0 count += 1
        2b/p ->6h < target so currmin = 6h
        hi = mid - 1
        mid = 1 + 1 // 2 = 1
        enter loop : while > 0...
        1b/h -> 10h
        compare min(res,  currmin) (10, 6)
        return


        """
        lo, hi = 1, max(piles)
        res = hi

        while lo <= hi:
            hours = 0
            mid = (lo + hi) // 2
            for pile in piles:
                hours += math.ceil(pile/mid)
            if hours <= h:
                res = min(res, mid)
                hi = mid - 1
            else: 
                lo = mid + 1
        return res


            


