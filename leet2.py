"""
https://leetcode.com/problems/convert-binary-number-in-a-linked-list-to-integer/

Convert Binary Number in a Linked List to Integer

Given head which is a reference node to a singly-linked list. The value of each node in the linked list is either 0 or 1. The linked list holds the binary representation of a number.

Return the decimal value of the number in the linked list.


Example 1:

Input: head = [1,0,1]
Output: 5
Explanation: (101) in base 2 = (5) in base 10


Constraints:

The Linked List is not empty.
Number of nodes will not exceed 30.
Each node's value is either 0 or 1.
"""

list_values = [1,0,0,1,1,0]
decimal_value = 38

#1.
# using the int() function
mylist = [1, 0, 0, 1, 1, 0]
print("The values in mylist are : " + str(mylist))
        
# binary list to integer conversion
result = 0
for digits in mylist:
    result = (result << 1) | digits

# result
print("The decimal value is : " + str(result))


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

#2.

class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        binary_arr = []
        current_node = head
        while current_node is not None:
            binary_arr.append(str(current_node.val))
            current_node = current_node.next
        print(binary_arr)
        return int("".join(binary_arr), 2)
        
        
        
        
        
        

        
        
        
        
        

            