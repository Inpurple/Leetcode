# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        return self.recur(head)
         
    
    def recur(self,k):
        """
        recur方法的顺序为先向下，后向上
        
        
        """
        if not k or not k.next:
            return k
        head1=k
        l=0
        while k:
            l+=1
            k=k.next
        
        k=head1
        h=1
        while h<l//2:
            h+=1
            k=k.next
        head2=k.next
        k.next=None
                   

        w=self.mergeTwoLists(self.recur(head1),self.recur(head2))
        return w
        
        
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: Lis
        Node
        :rtype: ListNode
        归并排序的合并的想法，结合链表的特点
        """
        prehead=ListNode(0)
        q=prehead
        while l1 and l2:
            if l1.val<=l2.val:
                q.next=l1
                l1=l1.next
            else:
                q.next=l2
                l2=l2.next
            q=q.next
            
        while l1:
            q.next=l1
            l1=l1.next
            q=q.next
        
        while l2:
            q.next=l2
            l2=l2.next
            q=q.next
            
        return prehead.next
            
        
