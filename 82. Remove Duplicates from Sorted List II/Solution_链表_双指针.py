# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy=ListNode(0)
        dummy.next=head
        
        pre=dummy
        cur=head
        
        while cur:
            while cur.next and cur.val==cur.next.val:
                cur=cur.next
            
            if pre.next==cur:
                pre=pre.next
            else:
                pre.next=cur.next
            cur=cur.next
            
            
        return dummy.next
        
