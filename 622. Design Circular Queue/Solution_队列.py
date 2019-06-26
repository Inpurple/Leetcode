class MyCircularQueue(object):

    def __init__(self, k):
        """
        Initialize your data structure here. Set the size of the queue to be k.
        :type k: int
        """
        self.que=[]
        self.len=k
        

    def enQueue(self, value):
        """
        Insert an element into the circular queue. Return true if the operation is successful.
        :type value: int
        :rtype: bool
        """
        if len(self.que)>=self.len:
            return False
        else:
            self.que.append(value)
            return True

    def deQueue(self):
        """
        Delete an element from the circular queue. Return true if the operation is successful.
        :rtype: bool
        """
        if not self.que:
            return False
        else:
            self.que.pop(0)
            return True

    def Front(self):
        """
        Get the front item from the queue.
        :rtype: int
        """
        if not self.que:
            return -1
        else:
            return self.que[0]

    def Rear(self):
        """
        Get the last item from the queue.
        :rtype: int
        """
        if not self.que:
            return -1
        else:
            return self.que[-1]

    def isEmpty(self):
        """
        Checks whether the circular queue is empty or not.
        :rtype: bool
        """
        return self.que==[]
        

    def isFull(self):
        """
        Checks whether the circular queue is full or not.
        :rtype: bool
        """
        return len(self.que)==self.len


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()
