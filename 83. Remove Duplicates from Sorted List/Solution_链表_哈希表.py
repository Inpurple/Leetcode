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
        cur=head
        pre=ListNode(0)
        pre.next=head
        while cur:
            if cur.val not in dic:
                dic[cur.val]=1
                cur=cur.next
                pre=pre.next
            else:   
                pre.next=cur.next
                cur=cur.next
        return head
