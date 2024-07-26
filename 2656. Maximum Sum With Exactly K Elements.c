int maximizeSum(int* nums, int n, int k){
    int sum=0;
    int max=nums[0];int ind=0;
    for(int i=0;i<n;i++){
        if(nums[i]>max){
            ind=i;
            max=nums[i];
        }
    }
    int temp=nums[n-1];
    nums[n-1]=nums[ind];
    nums[ind]=nums[n-1];
    for(int i=0;i<k;i++){
        sum=sum+nums[n-1];
        nums[n-1]=nums[n-1]+1;
    }
    return sum;
}