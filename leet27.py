class Solution:
    def removeElement(self, nums, val):
#          array called nums
#           value called val
# instantiate starting point
        i = 0
        
# iterate over the elements
# if the target number is not same as the value
# compare the first and second element and increment the first one by + 1 
        # else return

        for j, n in enumerate(nums):
            if n != val:
                nums[i] = nums[j]
                i += 1
        return i
    
        # Space Complexity = O(n) 
        # Time Complexity = O(n)
    
    removeElement(self, [3,2,2,3], 3)
    
    # Given nums = [3,2,2,3], val = 3