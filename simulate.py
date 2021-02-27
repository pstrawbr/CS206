import pybullet as p
import time
import pybullet_data
import pyrosim.pyrosim as pyrosim
import numpy
import random

physicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())
p.setGravity(0, 0, -9.8)

planeId = p.loadURDF("plane.urdf")
robot = p.loadURDF("body.urdf")
p.loadSDF("world.sdf")

pyrosim.Prepare_To_Simulate("body.urdf")

backLegSensorValues = numpy.zeros(1000)
frontLegSensorValues = numpy.zeros(1000)

amplitude = numpy.pi/4
frequency = 10
phaseOffset = 0

targetAngles = (amplitude * numpy.sin(frequency * numpy.linspace(-numpy.pi, numpy.pi, 1000) + phaseOffset))

for i in range(1000):
    p.stepSimulation()

    backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
    frontLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")

    pyrosim.Set_Motor_For_Joint(
        bodyIndex=robot,
        jointName="Torso_BackLeg",
        controlMode=p.POSITION_CONTROL,
        targetPosition=targetAngles[i],
        maxForce=30)
    pyrosim.Set_Motor_For_Joint(
        bodyIndex=robot,
        jointName="Torso_FrontLeg",
        controlMode=p.POSITION_CONTROL,
        targetPosition=targetAngles[i],
        maxForce=30)

    time.sleep(1/240)

numpy.save("data/backLegSense.npy", backLegSensorValues)
numpy.save("data/frontLegSense.npy", frontLegSensorValues)

p.disconnect()
