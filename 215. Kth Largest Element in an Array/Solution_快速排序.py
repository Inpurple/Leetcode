class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        return self.recur(0,len(nums)-1,nums,len(nums)-k)#注意审题，是第k大的，即第len(nums)-k个
        
    def partition(self,left,right,array):
        key=left
        while left<right:
            if array[right]<array[key] and array[left]>array[key]:
                array[right],array[left]=array[left],array[right]
            elif array[right]>=array[key]:
                right-=1
            elif array[left]<=array[key]:
                left+=1
        array[key],array[left]=array[left],array[key]
        return left
    
    def recur(self,left,right,array,k):
        mid=self.partition(left,right,array)
        if mid==k:
            return array[k]
        elif k>mid:
            return self.recur(mid+1,right,array,k)
        else:
            return self.recur(left,mid-1,array,k)
