from world import WORLD
from robot import ROBOT
import pybullet as p
import pybullet_data
import constants as c
import time


class SIMULATION:
    def __init__(self, directOrGUI, solutionID):
        if directOrGUI == "DIRECT":
            self.physicsClient = p.connect(p.DIRECT)
        else:
            self.physicsClient = p.connect(p.GUI)
        p.setAdditionalSearchPath(pybullet_data.getDataPath())
        p.setGravity(c.gravityX, c.gravityY, c.gravityZ)

        self.world = WORLD()
        self.robot = ROBOT(solutionID)

    def Run(self, directOrGUI):
        for t in range(c.iterations):
            p.stepSimulation()

            self.robot.Sense(t)
            self.robot.Think()
            self.robot.Act()
            if directOrGUI == 'GUI':
                time.sleep(c.sleepTime)


    def Get_Fitness(self, solutionID):
        self.robot.Get_Fitness(solutionID)

    def __del__(self):
        p.disconnect()
