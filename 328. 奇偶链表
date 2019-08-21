# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return None
        
        cur=head
        newcur=ListNode(head.val)
        newhead=newcur
        
        while cur and cur.next:
            if not cur.next.next:
                break
            cur=cur.next.next
            newcur.next=ListNode(cur.val)
            newcur=newcur.next
        
        
        cur=head.next
        
        
        while cur :
            newcur.next=ListNode(cur.val)
            if not cur.next:
                break
            cur=cur.next.next
            newcur=newcur.next
            
        return newhead
            
                
            
            
            
        
