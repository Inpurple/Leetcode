class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        """
        返回最大值的键
        时间复杂度：O(n)
        """
        counts = collections.Counter(nums)
        return max(counts.keys(), key=counts.get)

