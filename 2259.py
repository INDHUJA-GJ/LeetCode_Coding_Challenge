class Solution(object):
    def removeDigit(self, number, digit):
        n=number.count(digit)
        if n==1:
            return number.replace(digit, '', 1)
        num=number
        max=number.replace(digit, '', 1)
        for i in range(len(num)):
            if num[i]==digit:
                num=num[:i]+num[i+1:]
                if num>max:
                    max=num
                num=num[:i]+digit+num[i:]
        return max
