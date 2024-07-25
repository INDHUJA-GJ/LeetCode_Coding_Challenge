int minimumBoxes(int* ap, int a, int* ca, int c) {
    int sum=0;
    for(int i=0;i<a;i++){
        sum=sum+ap[i];
    }
    for(int i=0;i<c;i++){
        int ind=i;
        int min=ca[i];
        for(int j=i+1;j<c;j++){
            if(ca[j]>min){
                ind=j;
                min=ca[j];
            }
        }
        int temp=ca[i];
        ca[i]=ca[ind];
        ca[ind]=temp;
    }
    for(int i=0;i<c;i++){
        printf("%d ",ca[i]);
    }
    int count=0;int j=0;
    while(sum>0 && j<c){
        sum=sum-ca[j];
        j++;
        count++;
    }return count;
}