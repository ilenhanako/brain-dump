# 141 Linked List Cycle
# Given head(head of linked list), determine if the linked list has a cycle in it.
# Cycle: if there is some node in list that can be reached again by continuously following the next pointer. 
# Internally, pos is used to denote the index of the node that tail's next pointer is connected to.
# Note that pos is not passed as a parameter

# Return true if there is 

#Input: head = [3,2,0,-4], pos = 1 
#Output: True       why? There is a cycle in the linked list, where the tail connects to the 1st node (0-indexed).

#IDEA: 2pointer traverse list simultaneously: "slow" - move 1 step and "fast" - move 2 steps
# If there is a cycle, the fast pointer will catch up and meet the slow pointer. If no cycle, fast pointer will reach end of list

def hasCycle(head):
    turtle = head #slow
    rabbit = head #fast
    
    while rabbit and rabbit.next: #check that list is not empty, not null
        #if NOT CYCLE: loop will continue until rabbit or rabbit.next is null, indicating end of linked list
        #move tutle and rabbit
        turtle = turtle.next
        rabbit = rabbit.next.next
        
        #check whether fast and slow meet up
        if turtle == rabbit:
            return True
    return False
        