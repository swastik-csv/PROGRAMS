class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        if not nums:
            return 0
        
        # Pointer for the position of the last unique element
        slow = 0
        
        # Pointer to scan through the array
        for fast in range(1, len(nums)):
            if nums[fast] != nums[slow]:
                slow += 1
                nums[slow] = nums[fast]
                
        # Return the number of unique elements (index + 1)
        return slow + 1