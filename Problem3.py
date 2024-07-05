## Problem3 (https://leetcode.com/problems/search-a-2d-matrix-ii/)

class Solution:
    def searchMatrix(self, matrix, target):
        m = len(matrix)
        n = len(matrix[0])
        r, c = 0, n-1
        if not matrix or not matrix[0]:
            return False
            
        while r < m and c >= 0:
            if matrix[r][c] < target:
                r += 1
            elif matrix[r][c] > target:
                c -= 1

            else:
                return True
                
        return False

sol = Solution()
matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]]
target = 5
print(sol.searchMatrix(matrix,target))