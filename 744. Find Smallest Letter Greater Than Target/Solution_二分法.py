class Solution(object):
    def nextGreatestLetter(self, letters, target):
        """
        :type letters: List[str]
        :type target: str
        :rtype: str
        """
        small=0
        big=len(letters)-1
        print(small,big)
        while (big-small)>1:
            if letters[(small+big)//2]>target:

                big=(small+big)//2
            else:
                small=(small+big)//2
        
        print(small,big)
        print(letters[small],target,letters[small]>target)
        if letters[small]>target:
            return letters[small]
        elif letters[big]>target and letters[small]<=target:
            return letters[big]
        else:
            return letters[0]
