from extractControlDict import *
import instantaneousValues
from matplotlib import pyplot as plt

folderNumber = 0

while folderNumber <= endTime:
	if folderNumber == 0:
		folderNumber += (deltaT * writeInterval)
		continue
	# print folderNumber
	# import pdb; pdb.set_trace()
	pressure = instantaneousValues.pressureAtMoment(folderNumber)
	phi = instantaneousValues.phiAtMoment(folderNumber)
	vector = instantaneousValues.uAtMoment(folderNumber)
	# print pressure
	# plt.plot(pressure)
	# plt.show()
	# plt.figure('instant = ' + str(folderNumber))
	folderNumber += (deltaT * writeInterval)
