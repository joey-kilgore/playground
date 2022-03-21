#include <stdio.h>
#include <stdlib.h>

int main(int argc, char* argv[]) {
	FILE *fp;

	if(argc==1){ 
		printf("Please enter file path\n");
		exit(0);
	}

	fp = fopen(argv[1], "w+");
	fprintf(fp, "This is testing for fprintf...\n");
	fputs("This is testing for fputs...\n", fp);
	fclose(fp);
	
	return 0;
}
