class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2:
            return x
            
        left, right = 1, x // 2
        ans = 0
        
        while left <= right:
            mid = (left + right) // 2
            # Use multiplication instead of division to avoid floating-point inaccuracies
            if mid * mid <= x:
                ans = mid
                left = mid + 1  # Try to find a larger integer whose square is <= x
            else:
                right = mid - 1  # Mid's square is too large, search lower half
                
        return ans