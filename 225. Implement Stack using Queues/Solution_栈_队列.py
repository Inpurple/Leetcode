class MyStack(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.que1=[]
        self.que2=[]
        """
        思路：
        1.建立两个队列，每次压入时，将一个队列与栈元素顺序倒置，另一个队列为空方便下次入栈
        2.队列，其实就是一个先进先出的线性表，只能在队首执行删除操作，在队尾执行插入操作。用列表表示队列，
        可以用append()方法实现在队尾插入元素，用pop(0)方法实现在队首删除元素。

        >>> x=[]
        >>> x.append('a')
        >>> x
        ['a']
        >>> x.append('b')
        >>> x
        ['a', 'b']
        >>> x.pop(0)
        'a'
        >>> x.pop(0)
        'b'
        >>> x.pop(0)
        
        
        """

    def push(self, x):
        """
        Push element x onto stack.
        :type x: int
        :rtype: None
        """
        if self.que1==[]:
            self.que1.append(x)
            while self.que2:
                self.que1.append(self.que2.pop(0))
        elif self.que2==[]:
            self.que2.append(x)
            while self.que1:
                self.que2.append(self.que1.pop(0))

    def pop(self):
        """
        Removes the element on top of the stack and returns that element.
        :rtype: int
        """
        if self.que1:
            return self.que1.pop(0)
        else:
            return self.que2.pop(0)

    def top(self):
        """
        Get the top element.
        :rtype: int
        """
        if self.que1:
            return self.que1[0]
        else:
            return self.que2[0]
        

    def empty(self):
        """
        Returns whether the stack is empty.
        :rtype: bool
        """
        return self.que1==[] and self.que2==[]


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
