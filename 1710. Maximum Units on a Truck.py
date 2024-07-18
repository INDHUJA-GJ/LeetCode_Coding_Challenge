class Solution(object):
    def maximumUnits(self, b, t):
        b.sort(key=lambda x: x[1], reverse=True)
        res=0
        for i in b:
            if i[0]<=t:
                res=res+i[0]*i[1]
                t=t-i[0]
            else:
                res=res+t*i[1]
                t=0
        
        return res


        
