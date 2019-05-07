# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        快慢指针法。定义两个指针：快指针每次走一步；慢指针每次走两步。依次循环下去，如果链表存在环，那么快慢指针一定会有相等的时候。 
为了便于理解，你可以想象在操场跑步的两个人，一个快一个慢，那么他们一定会相遇（无论他们的起始点是不是在操场）。
        """
        if not head or not head.next:
            return False
        
        slow=head
        fast=head.next

        while slow.val != fast.val:

            slow=slow.next
            if fast.next:
                fast=fast.next.next
            else:
                 return False
            if not slow or not fast:
                return False
    
        return True
