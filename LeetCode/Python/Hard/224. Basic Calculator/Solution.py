class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        current_number = 0
        current_result = 0
        sign = 1  # 1 means positive, -1 means negative
        
        for char in s:
            if char.isdigit():
                current_number = current_number * 10 + int(char)
            elif char == '+':
                current_result += sign * current_number
                current_number = 0
                sign = 1
            elif char == '-':
                current_result += sign * current_number
                current_number = 0
                sign = -1
            elif char == '(':
                # Push the current result and the sign onto the stack before evaluating the inner expression
                stack.append(current_result)
                stack.append(sign)
                # Reset for the new sub-expression
                current_result = 0
                sign = 1
            elif char == ')':
                # First finish evaluating the last number inside the parentheses
                current_result += sign * current_number
                current_number = 0
                
                # Pop the sign before the parenthesis, then multiply with the sub-expression result
                current_result *= stack.pop()
                # Pop and add the result accumulated before the parenthesis started
                current_result += stack.pop()
                
        # Add any remaining number at the end of the string
        current_result += sign * current_number
        return current_result