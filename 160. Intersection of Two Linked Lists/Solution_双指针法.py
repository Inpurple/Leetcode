# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        1.双指针法的思路：指针P1和P2速度相同，路程相同，选择一种行走方案可在同节点处相遇，即先走完自己的链表，再走对方的链表。
        2.if 行内
            action if true else action
            =
            if true：
                action
            else
                action
        3.Python中if else简写出现"SyntaxError: can't assign to conditional expression"错误的解决方法将else后的“p1=”去掉。
        """
        
        p1=headA
        p2=headB
        while p1!=p2:
            p1=headB if p1==None else p1=p1.next
            p2=headA if p2==None else p2.next
        return p1
