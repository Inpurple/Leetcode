# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        
        反转链表+快慢指针法
        """
        
        fast=head
        slow=head
        pre=None
        

        while fast:
            fast=fast.next.next if fast.next else None
            slow=slow.next
            
        while slow:
            
            slow.next,pre,slow=pre,slow,slow.next
            
        while pre:
            if head.val!=pre.val:
                return False
            pre=pre.next
            head=head.next
            
        return True
        
