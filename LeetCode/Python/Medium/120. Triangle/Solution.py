class Solution:
    def minimumTotal(self, triangle: list[list[int]]) -> int:
        # Start with the bottom row of the triangle as our DP state
        dp = triangle[-1].copy()
        
        # Work our way up from the second-to-last row to the top
        for row in range(len(triangle) - 2, -1, -1):
            for col in range(len(triangle[row])):
                # Each element takes its own value plus the minimum of the two adjacent values below it
                dp[col] = triangle[row][col] + min(dp[col], dp[col + 1])
                
        # The top of the triangle will now contain the minimum path sum
        return dp[0]