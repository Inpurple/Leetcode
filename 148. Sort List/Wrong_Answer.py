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
        if not k or not k.next:
            return k
        h=k.next

        s=k
        f=k.next
        
        while s and s.next:
            s.next=s.next.next
            s=s.next
            if s:
                print("s",s.val)
            
        while f and f.next:
            f.next=f.next.next
            f=f.next
            if f:
                print("f",f.val) 
                
        #这样做是有问题的，因为通过s指针改变.next来得到一个相邻的链表，同时原有链表已经被改。
            
            
        w=self.mergeTwoLists(self.recur(k),self.recur(h))
        print(w.val)
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
            
