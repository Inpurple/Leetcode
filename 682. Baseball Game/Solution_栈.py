class Solution(object):
    def calPoints(self, ops):
        """
        :type ops: List[str]
        :rtype: int
        """
        sta=[]
        s=0
        for op in ops:
            
            if op.isdigit() or op.lstrip('-').isdigit():
                sta.append(int(op))
                s=s+int(op)
            elif op=="C":
                s=s-sta.pop()
            elif op=="D":
                s=s+sta[-1]*2
                sta.append(2*sta[-1])
            elif op=="+":
                s=s+sta[-1]+sta[-2]
                sta.append(sta[-1]+sta[-2])
        return s
 
