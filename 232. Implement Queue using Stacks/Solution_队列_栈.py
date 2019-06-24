class MyQueue(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.sta1=[]
        self.sta2=[]
        

    def push(self, x):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: None
        """
        while self.sta1:
            self.sta2.append(self.sta1.pop())
        self.sta2.append(x)
        while self.sta2:
            self.sta1.append(self.sta2.pop())

    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """
        return self.sta1.pop()
        

    def peek(self):
        """
        Get the front element.
        :rtype: int
        """
        return self.sta1[-1]

    def empty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """
        print("jud",self.sta1)
        if self.sta1:
            return False
        else:
            return True
        
        #return self.sta1==False 空列表不等于False，也不等于None
        
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
