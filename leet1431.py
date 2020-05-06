class Solution:
    def kidsWithCandies(self, candies, extraCandies):
        
        candies = [2,3,5,1,3]
        extraCandies = 3  
    
# return kid with largest stash of candy = fat_bastard
#     loop through list of kids with candy
# for each kid in list, 
# if the sum of what they already have + extraCandies >= fat_bastard
# return True for that kid, 
# else return False for that kid
# keep going to end of list
        
        max_candy = max(candies)
        for index in range(len(candies)):
            if candies[index] + extraCandies >= max_candy:
                yield True
            else:
                yield False
                
# Time complexity = O(n)
# Space complexity = O(n)
    
    kidsWithCandies([2,3,5,1,3], 3)