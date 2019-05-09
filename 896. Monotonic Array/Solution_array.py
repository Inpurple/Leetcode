class Solution(object):
    def isMonotonic(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        flag=3
        if A:
            for index in range(1,len(A)):
                if A[index]>A[index-1]:
                    if flag==3:
                        flag=0
                    elif flag==0:
                        flag=0
                    else:
                        print(False)
                        return False
                elif A[index]<A[index-1]:
                    if flag==3:
                        flag=1
                    elif flag==1:
                        flag=1
                    else:
                        return False
                else:
                    pass
            return True
        else:
            return False
