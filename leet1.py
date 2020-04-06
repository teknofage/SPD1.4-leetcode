"""
https://leetcode.com/problems/two-sum/

Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice."""

"""Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1]."""

given_nums = [2, 7, 11, 15]
target = 9

# Brute force way
def brute_force(given_nums, target):
    for i in range(len(given_nums)-1): #for each index in the length of the array
        for j in range(i+1, len(given_nums)): #for each index in the array after the index i
            if given_nums[i] + given_nums[j] == target: #if the two indices add up to the target
                print(given_nums[i], given_nums[j]) #print the two numbers at those indices
                return True
    return False #if no combination found, return False

print(brute_force(given_nums, target)) #print the function result



# Hash table way
#i = 0 #first element in hash table
#hash = dict() #create a dictionary
#hash[7] = 2 #first element in hash table is 2, difference between it and target is 7

#i = 1 #second element in hash table
#hash[2] = 7 #second element in hash table is 7, difference between it and target is 2

def hash_table(given_nums, target):
    hash = dict() #create a dictionary
    for i in range(len(given_nums)): #for each index in the range of the array
        if given_nums[i] in hash: #if the element is in the hash table
            print(hash[given_nums[i]], given_nums[i]) #print the corresponding indices from the hash table and the array
            return True 
        else:
            hash[target - given_nums[i]] = given_nums[i] #else if the element is not present in the hash table, subtract it from the target
    return False #if combination is not found
    
print(hash_table(given_nums, target))



#Adding elements together by incrementing
def two_sum(given_nums, target):
    i = 0
    j = len(given_nums) - 1
    
    while i <= j: 
        if given_nums[i] + given_nums[j] == target: #if the two numbers sum to make the target
            print(given_nums[i], given_nums[j]) #print the two numbers
            return True #and return True
        elif given_nums[i] + given_nums[j] < target: #if the two numbers sum to make less than the target
            i += 1 #increment i by 1
        else: 
            j -= 1 #decrement j by 1
    return False #pair not found

print(two_sum(given_nums, target))