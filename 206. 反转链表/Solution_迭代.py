# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        思路：
        迭代法：
        1.每次重复的操作是将指针 pre→cur 反向
        2.技巧：先将pre设为None
        """
        
        pre=None
        cur=head
        
        while cur:
            nex=cur.next
            cur.next=pre
            pre=cur
            cur=nex
            
        return pre
            
