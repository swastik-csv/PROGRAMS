class Solution:
    def maxArea(self, height: list[int]) -> int:
        left = 0
        right = len(height) - 1
        max_water = 0
        
        while left < right:
            # Calculate the width and height of the container
            width = right - left
            current_height = min(height[left], height[right])
            
            # Update the maximum water found so far
            max_water = max(max_water, width * current_height)
            
            # Move the pointer pointing to the shorter line inward
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
                
        return max_water