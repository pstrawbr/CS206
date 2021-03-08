from world import WORLD
from robot import ROBOT
import pybullet as p
import pybullet_data
import constants as c
import time


class SIMULATION:
    def __init__(self):
        self.physicsClient = p.connect(p.GUI)
        p.setAdditionalSearchPath(pybullet_data.getDataPath())
        p.setGravity(c.gravityX, c.gravityY, c.gravityZ)

        self.world = WORLD()
        self.robot = ROBOT()

    def Run(self):
        for t in range(c.iterations):
            p.stepSimulation()

            self.robot.Sense(t)
            self.robot.Act(t)

            time.sleep(c.sleepTime)

    def __del__(self):
        p.disconnect()
