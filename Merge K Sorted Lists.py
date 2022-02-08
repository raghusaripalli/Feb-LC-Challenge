/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    
    // Merge two linkedlists
    public ListNode mergeTwoLinkedLists(ListNode a, ListNode b)
    {
        // base cases
        if (a == null)
            return b;
        if (b == null)
            return a;
        ListNode dummy = new ListNode();
        ListNode head = dummy;
        while (a != null && b != null) {
            if (a.val < b.val) {
                head.next = a;
                a = a.next;
                head = head.next;
            }
            else if (a.val > b.val) {
                head.next = b;
                b = b.next;
                head = head.next;
            }
            else {
                head.next = a;
                a = a.next;
                head = head.next;
                head.next = b;
                b = b.next;
                head = head.next;
            }
        }
        
        while (a != null) {
            head.next = a;
            a = a.next;
            head = head.next;
        }
        
        while (b != null) {
            head.next = b;
            b = b.next;
            head = head.next;
        }
        
        return dummy.next;
    }
    
    public ListNode mergeKLists(ListNode[] lists) {
        int l = lists.length;
        if (l == 0)
            return null;
        while (l > 1)
        {
            for (int i = 0, j = 0; i < l; i+=2, j++) {
                if (i + 1 < l) {
                    ListNode merged = mergeTwoLinkedLists(lists[i], lists[i+1]);
                    lists[j] = merged;
                }
                else {
                    lists[j] = lists[i];
                }
            }
            l = (int) Math.ceil((l*1.0) / 2);
        }
        return lists[0];
    }
}
