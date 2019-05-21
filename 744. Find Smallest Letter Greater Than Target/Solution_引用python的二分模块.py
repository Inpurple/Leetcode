class Solution(object):
    def nextGreatestLetter(self, letters, target):
        """
        :type letters: List[str]
        :type target: str
        :rtype: str
        """
        index = bisect.bisect(letters, target)#将target插入在letters列表中，如果相等则插入右边。利用bisect.bisect方法的特点，index就为第一个大于target的索引值
        return letters[index % len(letters)]#余数可包括index==0，和index==len(letters)，的情况。index % len(letters)都为0
