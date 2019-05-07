class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        思路：

要求容器的容量，取决于 min(height[p1],height[p2])*(p2-p1)

关键问题是 短板，当然也有两板之间的距离，不过短板可以作为移动的判断条件，目的是使 短板更高一些

两个指针分别从首尾向中间缩，哪个板更短，就移动一下但面积只记录更大的面积
        为什么短板可以当做移动判断的条件：
如果移动长一点的短板，那么整个面积肯定是变小的，所以要想要面积变大必须移动短一点的短板，有可能通过比较面积的最大值变大
        """
        p1=0
        p2=len(height)-1
        
        maxarea=0
        while abs(p2-p1)>=1:
            area=min(height[p2],height[p1])*abs(p2-p1)
            maxarea=max(maxarea,area)
            
            if height[p1]> height[p2]:
                p2=p2-1
            else:
                p1=p1+1
        return maxarea  
