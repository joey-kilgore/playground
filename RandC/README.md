# R and C together sample  
The makefile creates the executable that R calls (it also creates a blank data.csv file). Then when R runs, it makes a system call to run the executable. The executable will save data to a file (in a csv format) and then R will read that file. From there graphs could be generated or other simulations could be called and new data could be generated.  
```  
make  
r callingCfromR.r
```
