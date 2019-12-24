# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        temp = 0
        
        head1 = head
        while head1:
            temp += 1
            head1 = head1.next
            
        if temp == n == 1:
            return None
        if temp -n +1 == 1:
            head = head.next
            return head
        
        print(temp)
        temp1 = 0
        head2 = head
        while temp1 < temp-n-1:
            head2 = head2.next
            temp1 += 1
            
        head2.next = head2.next.next
        
        return head