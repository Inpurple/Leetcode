class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        """线性时间复杂度，即在遍历此输入的参数时，for循环内的操作必须为常数时间复杂度
            1、数组的特点是：寻址容易，插入和删除困难；
            2、链表的特点是：寻址困难，插入和删除容易。
            3、Hash表的特点是：不论哈希表中有多少数据，查找、插入、删除（有时包括删除）只需要接近常量的时间即0(1）的时间级。

           在字典中不可以有相同的key，因为key是索引，给一个已经存在的key赋值即会改变它的值。
        """
    
        map_={}
        for num in nums:
            if num in map_:
                del map_[num] # 删除键是'num'的条目
            else:
                map_[num]=1
        for key in map_:
            return key
        



