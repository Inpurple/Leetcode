class MyCircularDeque(object):

    def __init__(self, k):
        """
        Initialize your data structure here. Set the size of the deque to be k.
        :type k: int
        """
        self.deque=[]
        self.len=k
        

    def insertFront(self, value):
        """
        Adds an item at the front of Deque. Return true if the operation is successful.
        :type value: int
        :rtype: bool
        """
        if len(self.deque)>=self.len:
            return False
        else:
            self.deque.insert(0,value)
            return True

    def insertLast(self, value):
        """
        Adds an item at the rear of Deque. Return true if the operation is successful.
        :type value: int
        :rtype: bool
        """
        if len(self.deque)>=self.len:
            return False
        else:
            self.deque.append(value)
            return True

    def deleteFront(self):
        """
        Deletes an item from the front of Deque. Return true if the operation is successful.
        :rtype: bool
        """
        if not self.deque:
            return False
        else:
            self.deque.pop(0)
            return True
        

    def deleteLast(self):
        """
        Deletes an item from the rear of Deque. Return true if the operation is successful.
        :rtype: bool
        """
        if not self.deque:
            return False
        else:
            self.deque.pop()
            return True

    def getFront(self):
        """
        Get the front item from the deque.
        :rtype: int
        """
        if not self.deque:
            return -1
        else:
            return self.deque[0]


    def getRear(self):
        """
        Get the last item from the deque.
        :rtype: int
        """
        if not self.deque:
            return -1
        else:
            return self.deque[-1]

        

    def isEmpty(self):
        """
        Checks whether the circular deque is empty or not.
        :rtype: bool
        """
        return self.deque==[]

    
    def isFull(self):
        """
        Checks whether the circular deque is full or not.
        :rtype: bool
        """
        return len(self.deque)==self.len


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()
 
