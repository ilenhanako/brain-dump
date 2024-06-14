#21. Merge Two Sorted Linked Lists
# Given heads of 2 sorted linked lists, list 1 and 2,
# Merge 2 lists into one sorted list. List made by splicing together nodes at first 2 lists.
# Return head of merged linked list

# Input: A = [5,10,15] , B = [2,3,20]
# Output: final = [2,3,5,10,15,20]

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeLinkedList(l1, l2):
    dummy = ListNode() #common technique to not worry about inserting edge case into empty list
    curr = dummy
    #case 1: both list not empty
    while l1 != None and l2 != None: #l1 and l2 not empty
        if l1.val < l2.val:
            curr.next = l1 # "adding l1 node to output" move pointer of curr to current node of l1
            l1 = l1.next #move pointer at l1 to next node
        elif l2.val < l1.val:
            curr.next = l2
            l2 = l2.next
        curr = curr.next #move to next node in merge list, ensure always point to last node so that we can add more nodes
    #case 2: one list empty, one list not empty
    if l1 != None:
        curr.next = l1
    if l2 != None:
        curr.next = l2
    return dummy.next
        
         
                        
                
                
        