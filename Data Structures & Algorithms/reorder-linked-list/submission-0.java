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
    public void reorderList(ListNode head) {

        //base case to check if the head is null
        if(head == null && head.next == null) return;

        // Step1: find the middle of  the list using two using fast and slow pointer
        ListNode fast = head, slow = head;

        while(fast != null && fast.next != null && fast.next.next != null){
            slow = slow.next;
            fast = fast.next.next;
        }


        //Step2 split the list from the middle and rotate the second halves

        ListNode curr = slow.next; 
        ListNode prev = null;

        slow.next = null;

        while(curr != null){
            ListNode temp = curr.next;
            curr.next = prev;
            prev = curr;
            curr = temp;
        }
        

        // Step3 Merge the two halves

        var first = head;
        var second = prev;

        while(second != null){
            var temp1 = first.next;
            var temp2 = second.next;

            first.next = second;
            second.next = temp1;

            first = temp1;
            second = temp2;
        }
        
    }
}
