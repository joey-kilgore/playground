# callingCfromR.r is a sample of how an R program can use the executables from
#   a compiled C/C++ program and run them to generate data, then bring the data
#   back into R to be analyzed

print("Hello from R")

# This is where the magic happens, essentially we simply send the bash command
#   to run the executable. By passing different arguments we can control the simulation

# system("./calledFromR.exe")
# system("./calledFromR.exe 2")
system("./calledFromR.exe 2 3")

# Gather the data generated from the executable
data <- read.csv(file = "data.csv", header=FALSE, sep=",")
x <- data[1,]
y <- data[2,]
print(x)
print(y)
