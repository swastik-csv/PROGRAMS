class Solution:
    def generateMatrix(self, n: int) -> list[list[int]]:
        # Initialize an n x n matrix with zeros
        matrix = [[0] * n for _ in range(n)]
        
        left, right = 0, n - 1
        top, bottom = 0, n - 1
        curr = 1
        
        while left <= right and top <= bottom:
            # 1. Traverse from left to right along the top row
            for col in range(left, right + 1):
                matrix[top][col] = curr
                curr += 1
            top += 1
            
            # 2. Traverse from top to bottom along the right column
            for row in range(top, bottom + 1):
                matrix[row][right] = curr
                curr += 1
            right -= 1
            
            # 3. Traverse from right to left along the bottom row (if applicable)
            if top <= bottom:
                for col in range(right, left - 1, -1):
                    matrix[bottom][col] = curr
                    curr += 1
                bottom -= 1
                
            # 4. Traverse from bottom to top along the left column (if applicable)
            if left <= right:
                for row in range(bottom, top - 1, -1):
                    matrix[row][left] = curr
                    curr += 1
                left += 1
                
        return matrix