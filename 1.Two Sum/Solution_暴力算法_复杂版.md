class Solution:
  def twoSum(self,nums，target):
    """
    :type nums:List[int]
    :type target:int
    :rtype :List[int]
    """
    
    for index1,nums1 in enumerate(nums):
        rest_nums=nums[index1+1:]
        for index2,nums2 in enumrate(rest_nums)：
            if nums1+nums2==target：
                if nums1=nums2：
                  return [nums.index(nums1),nums.index(nums2)]
                else:
                  """list重复的情况"""
                  index1=nums.index(nums)
                  nums[index1]=‘a’#替代法，将第一个相同的元素替代掉，方便下一条语句找到第二个相同的元素
                  index2=nums.index(nums)
                  return[index1,index2]
