# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        #initialize the pointers slow and fast
        slow = head
        fast = head

        #move slow by 1 step and fast by 2 steps
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        #if slow and fast meet together,then it's true
            if slow == fast:
                return True
        #if we exit the loop no cycle was found
        return False        


        
        