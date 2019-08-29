class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        while k>0:
            mi=float('inf')
            for  subarray in matrix:
                mi=min(mi,subarray[0])
            for  subarray in matrix:
                if subarray[0]==mi:
                    subarray.remove(mi)
                    if not subarray:
                        matrix.remove([])
                    break                 
            k-=1
        return mi
