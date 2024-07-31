class Solution(object):
    def nextGreatestLetter(self, lett, t):
        ind=0
        l=0
        r=len(lett)-1
        while l<=r:
            mid=l+(r-l)//2
            if lett[mid]>t:
                r=mid-1
                ind=mid
            else:
                l=mid+1
        return lett[ind]
        