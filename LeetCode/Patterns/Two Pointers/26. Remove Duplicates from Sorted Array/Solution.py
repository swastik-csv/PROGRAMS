class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        if not nums:
            return 0
        
        # Pointer for the last placed unique element
        slow = 0
        
        # Scan through the array with fast pointer
        for fast in range(1, len(nums)):
            if nums[fast] != nums[slow]:
                slow += 1
                nums[slow] = nums[fast]
                
        # The number of unique elements is slow + 1
        return slow + 1