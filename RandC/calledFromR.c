#include <stdio.h>
#include <stdlib.h>

// calledFromR.c takes in a number from as an argument and will
//  generate data.csv with multiples of that number
int main(int argc, char **argv){
    printf("Hello from C: %s\n",argv[0]);
    FILE *fp;
    fp = fopen("data.csv","w+");
    if(argc==2){
        int num = atoi(argv[1]);
        fprintf(fp, "%d,%d,%d,%d\n",num,num*2,num*3,num*4);
        fprintf(fp, "%d,%d,%d,%d\n",num,num*2,num*3,num*4);
    }
    else if(argc==3){
        int num = atoi(argv[1]);
        int num2 = atoi(argv[2]);
        fprintf(fp, "%d,%d,%d,%d\n",num,num*2,num*3,num*4);
        fprintf(fp, "%d,%d,%d,%d\n",num2,num2*2,num2*3,num2*4);
    }
    else{
        fprintf(fp, "1,2,3,4\n");
        fprintf(fp, "1,2,3,4\n");
    }
    fclose(fp);
    return 0;
}
