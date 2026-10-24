class Solution:
    def isValid(self, s: str) -> bool:
        # A valid string cannot have an odd number of characters
        if len(s) % 2 != 0:
            return False
            
        stack = []
        matching = {')': '(', '}': '{', ']': '['}
        
        for char in s:
            if char in matching:
                # If closing bracket, check if it matches the top of the stack
                if stack and stack[-1] == matching[char]:
                    stack.pop()
                else:
                    return False
            else:
                # Opening bracket
                stack.append(char)
                
        # Valid only if all opened brackets were closed
        return len(stack) == 0