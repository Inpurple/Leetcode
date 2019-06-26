class RecentCounter(object):

    def __init__(self):
        self.que=[]
        
        

    def ping(self, t):
        """
        :type t: int
        :rtype: int
        """
        if t:
            self.que.append(t)
            i=0
            while i<len(self.que)-1 and t-self.que[i]>3000:
                self.que.pop(0)#此处pop之后，无需修改指针
            #while语句是针对pop的情况，故从前往后数，如果小于3000，那么后面的也不需要比较了
            return len(self.que)


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)
