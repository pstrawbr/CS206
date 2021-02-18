import numpy
import matplotlib.pyplot as plt

backLegSensorValues = numpy.load("data/backLegSense.npy")
frontLegSensorValues = numpy.load("data/frontLegSense.npy")

plt.plot(backLegSensorValues, linewidth=4)
plt.plot(frontLegSensorValues)

plt.legend(('Back Leg', 'Front Leg'))

plt.show()
