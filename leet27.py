class Solution:
    def removeElement(self, nums: List[int], val: int):
#          array called nums
#           value called val
# instantiate starting point
        i = 0
        
# iterate over the elements
# if the target number is not same as the value
# compare the first and second element and increment the first one by + 1 
        # else return
        # Space Complexity = O(n) 
        # Time Complexity = O(n)
        for j, n in enumerate(nums):
            if n != val:
                nums[i] = nums[j]
                i += 1
        return i