# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        1.要对特殊节点操作有区分
        2.下一位操作pre=pre.next cur=cur.next 不一定使用于删除节点的操作
        """
        pre=ListNode(0)
        pre.next=head
        cur=head
        while cur:
            if cur.val==val:
                if cur==head:#头节点的情况
                    head=head.next
                    cur=cur.next
                    pre.next=head
                elif cur.next==None:#尾节点的情况
                    print(pre.val)
                    pre.next=None
                    break
                else:#中间节点的情况
                    pre.next=cur.next
                    cur=pre.next
            else:
                
                pre=pre.next
                cur=cur.next
            
        return head
