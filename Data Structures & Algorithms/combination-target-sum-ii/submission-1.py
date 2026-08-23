class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        """
        candidates = 
        [9,2,2,4,6,1,5], target = 8
             i   j
        9 > 8

        2 + 2 < 8
        2 + [2 + 4] = 8 add to res return

        2 + [2 + 6] > res return
        2 + 2 + 1 < res
        2 + 4 <  res 
        2  + 4 + 6 > res return
        2 + 6
        2 + 4 + 1 < res
        2 + 4 + 5 > res return
        4 + 6 > res return
        4 + 1 < res
        4 + 1 + 5 > res return
        4 + 5 > res ret

        """
        res = []
        candidates.sort()
        def backtrack(sub, start,total):
            if total == target:
                res.append(sub[:])
                return
            if total > target:
                return
            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i -1]:
                    continue
                sub.append(candidates[i])
                backtrack(sub, i + 1, total + candidates[i])
                sub.pop()
        backtrack([], 0, 0)
        return res

