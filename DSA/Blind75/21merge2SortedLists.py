#ERROROROROORORR

'''
21. Merge Two Sorted Lists
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.

In: l1 = [1,2,4], l2 = [3,4,5]
Out: 1 -> 1 -> 2 -> 3 -> 4 -> 5 -> None
'''

class ListNode:
    def __init__(self, val= 0, next= None):
        self.val = val # initializes the current node
        self.next = next #initialize next node

class Solution:
    def brute_force(self, l1, l2):
        #declare variables
        new_list = []
        
        # STEP 1: traverse both lists and copy the values into array
        # LOOP L1 and L2: check it's not empty 
        while l1:
            new_list.append(l1.val)
            l1 = l1.next
        
        while l2:
            new_list.append(l2.val)
            l2 = l2.next 
        
        #STEP 2: sort the array
        new_list.sort()
        print(new_list)
        
        # STEP 3: build new linked list base of the sorted value
        #create new linked list
        dummy = ListNode(0)
        current = dummy
        
        #Loop new_list
        for v in new_list:
            # create current new node
            current = ListNode(new_list)
            # move current to new node
            current = current.next        
        return dummy.next #return the head

# Build a linked list from a list
def build_list(arr):
    dummy = ListNode()
    current = dummy
    for val in arr:
        current.next = ListNode(val)
        current = current.next
    return dummy.next
    
sol = Solution()

l1 = build_list([1,2,4])
l2 = build_list([3,4,5])

result = sol.brute_force(l1, l2) #[1,2,3,4,4,5] 
print(result)