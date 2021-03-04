import pybullet as p
import time
import pybullet_data
import pyrosim.pyrosim as pyrosim
import numpy
import constants as c

physicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())
p.setGravity(c.gravityX, c.gravityY, c.gravityZ)

planeId = p.loadURDF("plane.urdf")
robot = p.loadURDF("body.urdf")
p.loadSDF("world.sdf")

pyrosim.Prepare_To_Simulate("body.urdf")

backLegSensorValues = numpy.zeros(c.iterations)
frontLegSensorValues = numpy.zeros(c.iterations)

backLegtargetAngles = c.amplitudeBack * numpy.sin(c.frequencyBack * numpy.linspace(-numpy.pi, numpy.pi, c.iterations) + c.phaseOffsetBack)


frontLegtargetAngles = c.amplitudeFront * numpy.sin(c.frequencyFront * numpy.linspace(-numpy.pi, numpy.pi, c.iterations) + c.phaseOffsetFront)

for i in range(c.iterations):
    p.stepSimulation()

    backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
    frontLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")

    pyrosim.Set_Motor_For_Joint(
        bodyIndex=robot,
        jointName="Torso_BackLeg",
        controlMode=p.POSITION_CONTROL,
        targetPosition=backLegtargetAngles[i],
        maxForce=c.maxForce)
    pyrosim.Set_Motor_For_Joint(
        bodyIndex=robot,
        jointName="Torso_FrontLeg",
        controlMode=p.POSITION_CONTROL,
        targetPosition=frontLegtargetAngles[i],
        maxForce=c.maxForce)

    time.sleep(c.sleepTime)

numpy.save("data/backLegSense.npy", backLegSensorValues)
numpy.save("data/frontLegSense.npy", frontLegSensorValues)

p.disconnect()
