#求和运算最后可能出现额外的进位，这一点很容易被遗忘

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        
        cur1=l1
        cur2=l2
        head=ListNode(-1)
        cur3=head
        m=0 #变量存储进位
        
        while cur1 or cur2:
            if cur1 and cur2:
                cur3.next=ListNode(cur1.val+cur2.val+m)
                cur1=cur1.next
                cur2=cur2.next
            elif not cur1:
                cur3.next=ListNode(cur2.val+m)
                cur2=cur2.next
            elif not cur2:
                cur3.next=ListNode(cur1.val+m)
                cur1=cur1.next
                
            cur3=cur3.next
            
            if cur3.val>=10:
                cur3.val=cur3.val-10
                m=1
            else:
                m=0
        if m==1:
            cur3.next=ListNode(1)
            
        return head.next
    
