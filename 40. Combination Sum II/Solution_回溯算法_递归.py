class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        注意的重点是，数组内的数不能重复使用，但数组内可以有重复的数，注意一下相同的数不要遍历两次产生重合的结果就好了。
        此时
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
                if i>0 and candidates[i-1]==candidates[i]:#必须是后面的值与前一个值对比，若相同则放弃此轮循环
                    continue #Python continue 语句跳出本次循环，而break跳出整个循环。
                self.dnf(candidates[i+1:],target,sum_list+[candidates[i]],result)#当前值要和后面所有的再一轮递归
