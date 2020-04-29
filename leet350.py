
def intersect(nums1, nums2):
    
    nums1 = [4,9,5] 
    nums2 = [9,4,9,8,4]
    expected_output = [4,9]
    
    # Variable Table
    # Variable . Value
    # nums1          . [4,9,5]
    # nums2          . [9,4,9,8,4] 
    # nums1 sorted   . [4,5,9]
    # nums2 sorted   . [4,4,8,9,9] 
    # pointer1       . 4
    #   pointer2     . 4
    #       output   . [4]
    # pointer1       . 5
    #   pointer2     . 4
    #       output   . [4]
    # pointer1       . 5
    #   pointer2     . 8
    #       output   . [4]
    # pointer1       . 9
    #   pointer2     . 8
    #       output   . [4]
    # pointer1       . 9
    #   pointer2     . 9
    #       output   . [4, 9]
    
    
    nums1.sort()
    nums2.sort()
    pointer1 = 0
    pointer2 = 0
    output = []
    while pointer1 < len(nums1) and pointer2 < len(nums2):
        if nums1[pointer1] == nums2[pointer2]:
            output.append(nums1[pointer1])
            pointer1 += 1
            pointer2 += 1
        elif nums1[pointer1] < nums2[pointer2]:
            pointer1 += 1
        else:
            pointer2 += 1
        
    print(list(output))
    return list(output)

intersect([4,9,5], [9,4,9,8,4])

if __name__ == '__main__':
    assert intersect([4,9,5], [9,4,9,8,4]) == [4,9]