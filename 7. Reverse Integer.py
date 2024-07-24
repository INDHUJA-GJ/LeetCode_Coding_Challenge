class Solution(object):
    def reverse(self, x):
        flag=0
        if x<0:
            flag=1
            x=x*-1
        num=str(x)
        num=num[::-1]
        if flag==1:
            num='-'+num
        res=int(num)
        if res > 2 ** 31 - 1 or res < -2 ** 31:
            return 0

        return int(num)
        
