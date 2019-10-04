print("Hello from R")
system("./calledFromR.exe")
data <- read.csv(file = "data.csv", header=FALSE, sep=",")
x <- data[1,]
print(data)
print(x)
