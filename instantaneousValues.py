from extractControlDict import *
from matplotlib import pyplot as plt

def pressureAtMoment(directoryNumber):
	pressure = []
	currentDirectory = parentDir + '/' + str(directoryNumber)
	pressureFile = open(os.path.join(currentDirectory, 'p'), 'r')
	flag = False
	for line in pressureFile:
		if line.startswith('('):
			flag = True
			continue
		if line.startswith(')'):
			flag = False
			continue
		if(flag == False):
			continue
		pressure.append(float(line))

	pressureFile.close()

	return pressure

def phiAtMoment(directoryNumber):
	phi = []
	currentDirectory = parentDir + '/' + str(directoryNumber)
	phiFile = open(os.path.join(currentDirectory, 'phi'), 'r')
	flag = False
	for line in phiFile:
		if line.startswith('('):
			flag = True
			continue
		if line.startswith(')'):
			flag = False
			continue
		if(flag == False):
			continue
		phi.append(float(line))

	phiFile.close()

	return phi

def uAtMoment(directoryNumber):
	vector = []
	x = []; y = []; z = []    

	currentDirectory = parentDir + '/' + str(directoryNumber)
	uFile = open(os.path.join(currentDirectory, 'U'), 'r')
	
	for line in uFile.readlines():
		if line[0]=='(' and line[-2]==')':
			spaceSplit = line.split(' ')
			x.append(float(spaceSplit[0].split('(')[-1]))
			y.append(float(spaceSplit[1]))
			z.append(float(spaceSplit[-1].split(')')[0]))

	vector.append(x)
	vector.append(y)
	vector.append(z)

	uFile.close()

	return vector