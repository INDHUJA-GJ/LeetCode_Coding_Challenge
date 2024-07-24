class Solution {
    public boolean isPalindrome(int x) {
        if(x<0){
            return false;
        }
        int ori=x;
        int num=0;
        while(x!=0){
            num=num*10+x%10;
            x=x/10;
        }
        if(ori==num){
            return true;
        }
        return false;
    }
}