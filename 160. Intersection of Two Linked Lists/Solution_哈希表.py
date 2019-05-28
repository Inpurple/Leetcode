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
        除相交节点外，每个节点都不同，故可以用哈希表来解决
        可以用作字典键值的数据类型：所有python自带类型中，除了list、dict、set和内部至少带有上述三种类型之一的tuple之外，其余的对象都能当key
        """
        dic={}
        cur1=headA
        cur2=headB
        while cur1:
            dic[cur1]=1
            cur1=cur1.next
            
        while cur2:
            if cur2 in dic:
                return cur2
            cur2=cur2.next
            
        return None
