
import time
import pyrosim.pyrosim as pyrosim
import numpy
from simulation import SIMULATION

'''



pyrosim.Prepare_To_Simulate("body.urdf")

backLegSensorValues = numpy.zeros(c.iterations)
frontLegSensorValues = numpy.zeros(c.iterations)

backLegtargetAngles = c.amplitudeBack * numpy.sin(c.frequencyBack * numpy.linspace(-numpy.pi, numpy.pi, c.iterations) + c.phaseOffsetBack)


frontLegtargetAngles = c.amplitudeFront * numpy.sin(c.frequencyFront * numpy.linspace(-numpy.pi, numpy.pi, c.iterations) + c.phaseOffsetFront)



numpy.save("data/backLegSense.npy", backLegSensorValues)
numpy.save("data/frontLegSense.npy", frontLegSensorValues)

p.disconnect()
'''
simulation = SIMULATION()
simulation.Run()
