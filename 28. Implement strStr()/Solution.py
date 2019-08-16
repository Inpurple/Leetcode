class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if needle in haystack:
            haystack=haystack.replace(needle,"_")
            lis=list(haystack)
            return haystack.index("_")
        else:
            return -1
