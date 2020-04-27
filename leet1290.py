
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

head = [1,0,1]
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
            new_list.append(str(node.val))
            print(new_list)
            node = node.next
            print(new_list)
        
        bin_number = ''.join(new_list)
        return int(bin_number, 2)
    
