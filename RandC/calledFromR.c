#include <stdio.h>
#include <stdlib.h>

int main(){
    printf("Hello from C\n");
    FILE *fp;
    fp = fopen("data.csv","w+");
    fprintf(fp, "1,2,3,4\n");
    fclose(fp);
    return 0;
}
