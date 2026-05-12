class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        count = len(matrix[0])
        for i in range(len(matrix)-1,-1,-1):
            head = matrix[i][0]
            if target < head:
                continue
            elif target > head:
                for j in range(0,count):
                    if target == matrix[i][j]:
                        return True
            elif target == head:
                return True
        return False
