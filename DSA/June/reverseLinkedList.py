# 206 Reverse Linked list, Easy
# Given head of singly linked list, reverse the list and return reversed list.
# Input: 1 -> 2 -> 3 -> 4 -> 5
# Output: 5 -> 4 -> 3 -> 2 -> 1

#Iteration 1: null <- 1   2 -> 3 -> 4 -> 5 -> null
#Iteration 2: null <- 1 <- 2   3 -> 4 -> 5 -> null

def reverseLinkedList(head):
    #2 pointer, curr and prev
    curr = head #initialise at head
    prev = None # initialise at null
    
    while not curr:
        prev = curr
        curr = curr.next()
    return prev

head = [1, 2, 3, 4, 5]
print(reverseLinkedList(head))

