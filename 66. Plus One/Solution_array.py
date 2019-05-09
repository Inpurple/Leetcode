class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        #join方法只能string，不能对int
        """
        
        n=len(digits)
        count=0
        rlist=[]
        for index,num in enumerate (digits):
            x=num*(10**(n-index-1))
            count=count+x
        print(str(count+1))
        for num in list(str(count+1)):
            rlist.append(int(num))
        return rlist
