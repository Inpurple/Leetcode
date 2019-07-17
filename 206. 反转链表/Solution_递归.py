# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head: ListNode,tail=None) -> ListNode:
        if head:
            head.next,tail,head=tail,head,head.next#这样做可以避免先后顺序导致赋值有错误
            '''
            head.next=tail
            tail=head
            head=head.next
            错误赋值
            '''
        return self.reverseList(head,tail) if head else tail
        
