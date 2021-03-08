from world import WORLD
from robot import ROBOT
import pybullet as p
import pybullet_data
import constants as c
import time
import pyrosim.pyrosim as pyrosim


class SIMULATION:
    def __init__(self):
        self.physicsClient = p.connect(p.GUI)
        p.setAdditionalSearchPath(pybullet_data.getDataPath())
        p.setGravity(c.gravityX, c.gravityY, c.gravityZ)
        pyrosim.Prepare_To_Simulate("body.urdf")

        self.world = WORLD()
        self.robot = ROBOT()

    def Run(self):
        for t in range(c.iterations):

            p.stepSimulation()

            ROBOT.Sense(self.robot, t)
            ROBOT.Act(self.robot, t, self.world.robot)

            time.sleep(c.sleepTime)

    def __del__(self):

        p.disconnect()
