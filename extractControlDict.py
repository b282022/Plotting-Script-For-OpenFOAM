import os

parentDir = os.getcwd()    
startTime = 0.0
endTime = 0.0
deltaT = 0.0
writeInterval = 0.0                
        
        
controlDictFile = open(os.path.join(parentDir+'/system', "controlDict"), 'r')

for line in controlDictFile.readlines():
    if line.startswith("startTime"):
        startTime = float(line.split(' ')[-1].split(';')[0]);
    elif line.startswith("endTime"):
        endTime =  float(line.split(' ')[-1].split(';')[0]);
    elif line.startswith("deltaT"):
        deltaT = float(line.split(' ')[-1].split(';')[0])
    elif line.startswith("writeInterval"):
        writeInterval = float(line.split(' ')[-1].split(';')[0])

controlDictFile.close()
