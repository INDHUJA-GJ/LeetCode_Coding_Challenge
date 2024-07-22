int projectionArea(int** grid, int r, int* c) {
    int res=0;
    for(int i=0;i<r;i++){
        for(int j=0;j<c[i];j++){
            if(grid[i][j]!=0)
            res=res+1;
        }
    }
    for(int i=0;i<r;i++){
        int max=0;
        for(int j=0;j<c[i];j++){
            if(grid[i][j]>max)
            max=grid[i][j];
        }
        res=res+max;
    }
    for(int i=0;i<c[0];i++){
        int max=0;
        for(int j=0;j<r;j++){
            if(grid[j][i]>max)
            max=grid[j][i];
        }
        res=res+max;
    }
    return res;
}
