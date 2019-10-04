#include <omp.h>
#include <stdio.h>
#include <stdlib.h>

int someMath(int num,int i){
    num = num * num * num * i;
    return num;
}

int main(int argc, char** argv){
    int nthreads, tid;
    int i;
    int num = atoi(argv[1]);
    int data[10000];

    #pragma omp parallel
    {
    #pragma omp for
    for(i=0; i<10000; i++){
        data[i] = someMath(num,i);
    }
    }

    FILE *fp;
    fp = fopen("data.csv","w+");
    for(i=0; i<10000; i++){
        fprintf(fp, "%d,",data[i]);
    }
    fprintf(fp, "\n");
    for(i=0; i<10000; i++){
        fprintf(fp, "%d,",data[i]);
    }
    fprintf(fp, "\n");
    fclose(fp);
}
