class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]

        字典键值的同时遍历： enumerate(dic) 或者 dic.items()
        数组的同时遍历：enumerate(list)
        """
        if not candidates or not target:
            return []
        else:
            result=[]
            candidates.sort()
            self.dnf(candidates,target,[],result)
            return result    
        
    def dnf(self,candidates,target,sum_list,result):
        if sum(sum_list)>target:
            return
        elif sum(sum_list)==target:
            result.append(sum_list)
        else:
            for i in range(len(candidates)):
                self.dnf(candidates[i:],target,sum_list+[candidates[i]],result)#list的相加
