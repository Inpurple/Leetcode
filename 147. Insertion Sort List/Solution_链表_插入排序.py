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
        指针的插入排序是一种简单直观的排序算法，它的工作原理是通过构建有序序列，对于未排序数据，在已排序序列中从前向后扫描，找到相应位置并插入。插入排序的实现上，通常采用 in-place 排序（即只需用到O(1)的额外空间的排序）。

用指针 p 逐一向后遍历

0. 申请一个 dummyHead 节点，其下一个节点指向头结点。如果要在头结点出插入，dummyHead 会给我们带来便利

1. 当 p 的值不大于下一节点值，就进行遍历下一节点

2. 当 p 的值大于下一节点，那么就将p 的下一节点取出，从前向后扫描，在第一个比它的值大的节点之前插入该节点

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
            
