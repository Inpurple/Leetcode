class MinStack(object):
    """min()为python内置方法，时间复杂度为O(n),所以一定要利用栈的特性，想别的方法。
        算法：
        1.首先在此方法中构造出两个以顺序表为形式的栈，一个用于正常情况，另一个在各种操作的时候记住最小值，这样就可以回避遍历的算法
        2.压栈，最小栈小的在上，大的在下，如果进来的比顶端的值大，则不压栈
        3.出栈，如果两个栈的顶端的值 都是相同的，则出栈
        4.顶端值正常，最小方法，直接输出顶端值即可
        tips：
        1.注意list[-1]，以及list.pop()，一定要排除空的情况
        2.注意list.pop()的操作会影响list，一定要注意步骤
        2.注意如果进来了相同的值，也要压栈。所以在压栈方法中，是大于等于而不是大于
    """
    
    
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.__list=[]
        self.__min__list=[]

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        self.__list.append(x)
        if self.__min__list:
            if self.__min__list[-1]>=x:
                self.__min__list.append(x)
        else:#考虑最小栈为空的特殊情况
            self.__min__list.append(x)

    def pop(self):
        """
        :rtype: void
        """
        if self.__list and self.__min__list:
            if self.__list[-1]==self.__min__list[-1]:
                self.__min__list.pop()
                self.__list.pop()
            else:
                self.__list.pop()

    def top(self):
        """
        :rtype: int
        """
        if self.__list:
            return self.__list[-1]
        else:
            return None

    def getMin(self):
        """
        :rtype: int
        
        """
        if self.__min__list:
            return self.__min__list[-1]
        else:
            return None

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
