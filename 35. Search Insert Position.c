int searchInsert(int* nums, int n, int t) {
    int l=0;
    int r=n-1;
    int ind=-1;
    while(l<=r){
        int mid=l+(r-l)/2;
        if(nums[mid]<=t){
            ind=mid;
            if(nums[mid]==t)
            return mid;
            l=mid+1;
        }
        else{
            r=mid-1;
        }
    } return ind+1;
    
}