# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
        if not head or not head.next:
            return head
        
        prehead=ListNode(0)#创建虚拟节点，方便从头节点插入
        prehead.next=head
        cur=head
        
        while cur and cur.next:
            if cur.next.val>=cur.val:
                cur=cur.next
            else:
                temp=cur.next
                cur.next=cur.next.next  #先利用链表的方法删掉目标节点
                
                q=prehead
                while q.next.val<=temp.val:#从q.next开始，即方便从头结点插入，又避开与prehead节点的值比较
                    q=q.next
                temp.next=q.next
                q.next=temp
        return prehead.next
            
