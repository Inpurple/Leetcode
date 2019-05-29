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
        cur=head
        if head==None or head.next==None:#排除空链表和单链表
            return head
        else:
            while cur and cur.next!=None:#遍历，因为看当前结点和下一个节点是否为相同值，所以排除遍历完和遍历到倒数第一个的情况
                if cur.val==cur.next.val:#比较当前结点和下一结点是否为相同值
                    if cur==head:#pre是none的情况
                        head=cur.next
                    else:
                        pre.next=cur.next#删除节点的策略是将前一个结点的next指向此结点的后一个
                    cur=cur.next
                else:
                    pre=cur
                    cur=cur.next
            return head
