# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        """
        回文链表，不一定链表节点数必须为偶数
        """
        
        cur=head
        lis=[]
        
        while cur:
            lis.append(cur.val)
            cur=cur.next
            
        p1=0
        p2=len(lis)-1
        
        while p1<=p2:
            if lis[p1]!=lis[p2]:
                return False
            else:
                p1+=1
                p2-=1
        return True
            
            
        
    
