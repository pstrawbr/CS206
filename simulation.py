from world import WORLD
from robot import ROBOT
import pybullet as p
import pybullet_data
import constants as c
import time
import pyrosim.pyrosim as pyrosim

#TODO Stuck on 47

class SIMULATION:
    def __init__(self):
        self.physicsClient = p.connect(p.GUI)
        p.setAdditionalSearchPath(pybullet_data.getDataPath())
        p.setGravity(c.gravityX, c.gravityY, c.gravityZ)

        self.world = WORLD()
        self.robot = ROBOT()

    def Run(self):
        for i in range(c.iterations):

            p.stepSimulation()
            '''
            self.backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
            self.frontLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")

            pyrosim.Set_Motor_For_Joint(
                bodyIndex=self.robot,
                jointName="Torso_BackLeg",
                controlMode=p.POSITION_CONTROL,
                targetPosition=self.backLegtargetAngles[i],
                maxForce=c.maxForce)
            pyrosim.Set_Motor_For_Joint(
                bodyIndex=self.robot,
                jointName="Torso_FrontLeg",
                controlMode=p.POSITION_CONTROL,
                targetPosition=self.frontLegtargetAngles[i],
                maxForce=c.maxForce)
'''
            time.sleep(c.sleepTime)

    def __del__(self):
        p.disconnect()