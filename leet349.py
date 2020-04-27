class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        #         given two arrays
        # return single instance of common elements
#         solution1
        # return (set(nums1) & set(nums2))
        
#         solution2
        
        # iterate through nums1 and add numbers to a hash table
        # iterate through nums2 and compare to hash table
        # add duplicates to new list, as long as that list does             not already contain them
#         h_set = set()
#         output = set()
#         for x in nums1:
#             h_set.add(x)
#         for y in nums2:
#             if y in h_set and y not in output:
#                 output.add(y)
                    
#         return list(output)
    
#     solution3
        # search both lists 
        # return one instance of common elements
        # output = set()
        # for x in nums1:
        #     for y in nums2:
        #         if x == y:
        #             output.add(x)
        # return list(output)
        
        
        # solution4
#        edit one list by removing duplicates and numbers on in both lists until it is the output


#         solution5
#         sort array in place
        nums1.sort()
        for x in nums1:
            for y in nums2: