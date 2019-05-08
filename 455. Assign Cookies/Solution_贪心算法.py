class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        小找小，while语句更少，更节约时间
        注意如果需要不规则修改指针用while
        
        
        思路：
        1、首先把两个数组排序
        2、如果当前满足感小于等于饼干，两个指针都后移，否则，只有满足感后移，然后再和当期前的满足感比较
        3、最后返回指向孩子满足感指针的指针位置
        """
        
        j=0
        i=0
        g.sort()
        s.sort()
        while j<len(s):
            if i>=len(g) :
                return i
            else:
                if s[j]>=g[i]:
                    
                    i=i+1
                    j=j+1
                else:
                    j=j+1
                    
        return i
