import numpy
import matplotlib.pyplot as plt

# backLegSensorValues = numpy.load("data/backLegSense.npy")
# frontLegSensorValues = numpy.load("data/frontLegSense.npy")
#
# plt.plot(backLegSensorValues, linewidth=4)
# plt.plot(frontLegSensorValues)
#
# plt.legend(('Back Leg', 'Front Leg'))


backLegtargetAngles = numpy.load("data/backLegtargetAngles.npy")
frontLegtargetAngles = numpy.load("data/frontLegtargetAngles.npy")

plt.plot(backLegtargetAngles)
plt.plot(frontLegtargetAngles)
plt.legend(('Back Leg', 'Front Leg'))

plt.show()
