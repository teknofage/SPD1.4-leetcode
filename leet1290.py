
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
        # self.next = None


    # iterate over ListNode
    # set head to 0
    # set node to next node ex node_next
    # append value of each node to new list
    # convert new list binary values to decimal
    # return value of converted value
class Solution:
    def getDecimalValue(self, head: ListNode) ->int:
    
    node = head
    new_list = []
    while node!= None:
        new_list.append(node.val)
        node = node.next
    bin_number = int("".join(new_list), 2)
    return decimal(bin_number)