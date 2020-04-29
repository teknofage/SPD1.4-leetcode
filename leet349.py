class Solution:
    def intersection(nums1, nums2):
        
        nums1 = [1,2,2,1]
        nums2 = [2,2] 
        expected_output = [2] 
        
        """given two arrays
        return single instance of common elements"""
        
#       Solution1
        #       return (set(nums1) & set(nums2))
        
        
#       Solution2
        """iterate through nums1 and add numbers to a hash table
        iterate through nums2 and compare to hash table
        add duplicates to new list, as long as that list does not 
        already contain them"""
        
        # Variable Table
        # Variable . Value
        # nums1    . [1,2,2,1]
        # nums2    . [2,2] 
        # x1       . 1
        # h_set    . (1)
        # x2       . 2
        # h_set    . (1,2)
        # x3       . 2
        # h_set    . (1,2,2)
        # x4       . 1
        # h_set    . (1,2,2,1)
        # y1       . 2
        # output   . [2]
        # y2       . 2
        # output   . [2]
        
        
        h_set = set()
        output = set()
        for x in nums1:
            h_set.add(x)
        for y in nums2:
            if y in h_set and y not in output:
                output.add(y)
                
        print(list(output))
        return list(output)
    
#       Solution3
        """search both lists 
        return one instance of common elements"""
        
        # Variable Table
        # Variable . Value
        # nums1    . [1,2,2,1]
        # nums2    . [2,2] 
        # x1       . 1
        # x2       . 2
        # x3       . 2
        # x4       . 1
        # y1       . 2
        # output   . [2]
        # y2       . 2
        # output   . [2]
        
        # output = set()
        # for x in nums1:
        #     for y in nums2:
        #         if x == y:
        #             output.add(x)
        # return list(output)
        
        
#       Solution4
#        edit one list by removing duplicates and numbers 
#       on in both lists until it is the output


#         Solution5
# #         sort array in place
#         nums1.sort()
#         for x in nums1:
#             for y in nums2:

    intersection([1,2,2,1], [2,2])