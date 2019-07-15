# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        遍历一次链表，将数据记录在lis中，再反转，再重新赋值
        方法略土
        :type head: ListNode
        :rtype: ListNode
        """
        cur=head
        lis=[]
        while cur:
            lis.append(cur.val)
            cur=cur.next
        
        
        lis.reverse()
        print(lis)
        
        cur=head
        i=0
        while cur and i<=len(lis)-1:
            cur.val=lis[i]
            cur=cur.next
            i+=1
        
        return head
