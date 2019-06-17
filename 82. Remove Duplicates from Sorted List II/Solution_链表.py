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
        dic={}
        dup={}
        cur1=head
        while cur1:
            if cur1.val in dic:
                dup[cur1.val]=1
            else:
                dic[cur1.val]=1
            cur1=cur1.next

        p=ListNode(0)
        p.next=head
        pre=p
        cur=head
        while cur:
            if cur.val in dup:
                pre.next=cur.next
                cur=cur.next
            else:
                pre=pre.next
                cur=cur.next
        return p.next
            
