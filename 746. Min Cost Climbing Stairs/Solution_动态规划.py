class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        算法：
        1.此题顶端意思是到达索引为len(cost)，而不是len(cost)-1
        2.通过动态规划，从0到最后一个阶梯，储存停在阶梯上的最小的值。
        """
        dq=[]
        for i in range(0,len(cost)):#遍历停留在这个数的时候
            if i==0:
                dq.insert(0,0)
            elif i==1:
                dq.insert(1,0)
            else:
                dq.insert(i,min(dq[i-2]+cost[i-2],dq[i-1]+cost[i-1]))
        return min(dq[len(cost)-1]+cost[len(cost)-1],dq[len(cost)-2]+cost[len(cost)-2])
