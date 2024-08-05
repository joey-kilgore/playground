import subprocess


for i in range(0,10):
	fileNum = i
	fileName = 'outputFiles/output'+str(fileNum)+'.txt'
	argList = ['./writeToFile', fileName]
	
	p = subprocess.Popen(argList)
	
	p.wait()
	
	f = open(fileName, "r")
	print("File: " + fileName)
	print(f.read())
