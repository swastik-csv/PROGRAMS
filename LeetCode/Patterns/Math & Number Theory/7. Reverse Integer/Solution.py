class Solution:
    def reverse(self, x: int) -> int:
        # Define 32-bit integer limits
        INT_MIN, INT_MAX = -2**31, 2**31 - 1
        
        res = 0
        # Handle negative numbers by keeping track of the sign
        sign = -1 if x < 0 else 1
        x = abs(x)
        
        while x != 0:
            digit = x % 10
            x //= 10
            
            # Check for overflow before multiplying by 10 and adding the digit
            if res > (INT_MAX - digit) // 10:
                return 0
                
            res = res * 10 + digit
            
        return sign * res