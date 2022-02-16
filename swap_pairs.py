# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        dummy = ListNode()
        dummy.next = head;
        prev = dummy
        cur = head
        
        while cur is not None and cur.next is not None:
            fwd = cur.next;
            cur.next = fwd.next;
            fwd.next = cur;
            prev.next = fwd;
            
            prev = cur;
            cur = cur.next
            
                
        
        return dummy.next;
