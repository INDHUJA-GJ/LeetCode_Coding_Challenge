int minimumPushes(char* word) {
    int l=strlen(word);
    if(l<=8)
    return l;
    if(l>8 && l<=16){
        l=l-8;
        l=l*2+8;
        return l;
    }
    else if(l>16 && l<=24 ){
        l=l-16;
        l=l*3+8+16;
    }
    else{
        if(l==25){
        l=l-16;
        l=l*3+8+16+1;

    }
    else{
        l=l-16;
        l=l*3+8+16+1+1;}}
    return l;
}