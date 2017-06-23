from extractControlDict import *
import instantaneousValues
from matplotlib import pyplot as plt

folderNumber = 0

while folderNumber <= endTime:
	print folderNumber
	pressure = individualPressure.pressureAtMoment(folderNumber)
	phi = individualPressure.phiAtMoment(folderNumber)
	print pressure
	# plt.plot(pressure)
	# plt.show()
	# plt.figure('instant = ' + str(folderNumber))
	folderNumber += (deltaT * writeInterval)
