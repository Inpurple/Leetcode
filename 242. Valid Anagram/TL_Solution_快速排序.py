class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        lists=list(s)
        listt=list(t)
        self.quicksort_recur(0,len(t)-1,listt)
        self.quicksort_recur(0,len(s)-1,lists)
        print(listt==lists)
        return(listt==lists)
    
    def partition(self,left,right,array):
        key=left
        while left<right:
            if array[left]>array[key] and array[right]<array[key]:
                array[left],array[right]=array[right],array[left]
                #left=left+1
                #right=right-1
            elif array[right]>=array[key]:#等号容易忘掉
                right=right-1
            elif array[left]<=array[key]:
                left=left+1
        array[key],array[right]=array[right],array[key]
        return right
    
    def quicksort_recur(self,left,right,array):
        if left>=right:
            return 
        else:
            mid=self.partition(left,right,array)
            self.quicksort_recur(left,mid-1,array)
            self.quicksort_recur(mid+1,right,array)
