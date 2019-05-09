class MyQueue(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack_i=[]
        self.stack_o=[]

    def push(self, x):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: void
        """
        self.stack_i.append(x)
        
        

    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """
        """
        算法：
        1)建立两个栈input与output，其中input用于入队列，output用于出队列；
        2)当元素要入队列时，直接当元素压入input中；
        3)当元素要出队列时，先判断output中是否有元素。若是有，可以直接将output中的栈顶元素出队列；若是没有，则先将input中的  元素入到output中，再将output的栈顶元素出队列；
        4）判断队列是否为空，依次判断input与output是否为空，若有其中一个栈不为空，则队列就不为空
        
        Notes：
        self.stack_o==None and self.stack_i==None return True容易出错
        self.stack_o or self.stack_i return False更好
        
        """
        if self.stack_o:
             return self.stack_o.pop()      
        else:
            while self.stack_i:
                self.stack_o.append(self.stack_i.pop())
            return self.stack_o.pop()
                

    def peek(self):
        """
        Get the front element.
        :rtype: int
        """
        if self.stack_o:
            return self.stack_o[-1]#不知道是否合乎题目要求
        else:
            #return self.stack_i[0]#不知道是否合乎题目要求
            while self.stack_i:
                self.stack_o.append(self.stack_i.pop())
            return self.stack_o[-1]
        
    def empty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """
        
        if self.stack_o or self.stack_i:
            return False
        else:
            return True
