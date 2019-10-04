all: calledFromR.exe openmp

calledFromR.exe: calledFromR.c
	touch data.csv
	gcc -o calledFromR.exe calledFromR.c

openmp: openMP.c
	gcc -o openMP -fopenmp openMP.c

clean:
	rm data.csv
	rm calledFromR.exe
	rm openMP
