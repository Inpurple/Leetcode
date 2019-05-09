class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        """
        算法很简单，但是，要注意的是list中插入元素，insert更为适用，并且不能像字典一样直接索引赋值来增加元素
        """
        
        in_list=[]
        for n in range(numRows):
            in_list.insert(n,[])
            for i in range(0,n+1):
                if i >0 and i< n:
                    value=in_list[n-1][i-1]+in_list[n-1][i]
                    in_list[n].insert(i,value)
                else:
                    in_list[n].insert(i,1)
        return in_list
