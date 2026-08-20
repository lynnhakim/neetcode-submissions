class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        """
        1  4  6  10
        11 12 13 14
        16 18 20 21

        m: rows, n col -> 3x4 = 12
        1. mid index :12 // 2 -> 6 //3 = 2, 6//4 = 1 [2, 1]
        2. compare to target: matrix[2][1] = 12 > target
            a. greater: mid = left + 1 -> 3x4 -> 2+1 x 1 + 1 = 6
        1. mid index: 6 // 2 = 3 -> 3//3 = 1 , 3//4 = 0 [3, 0]
        2. matrix[1][0] = 10 < targetr 
            b. 

        """
        m, n = len(matrix), len(matrix[0])
        lo, hi = 0, m* n - 1
        while lo <= hi : 
            mid =(lo + hi)// 2
            row, col = mid // n, mid % n
            if matrix[row][col] == target: 
                return True
            elif matrix[row][col] > target: 
                hi = mid - 1
            else: 
                lo = mid + 1

        return False

        
