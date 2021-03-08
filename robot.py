import pyrosim.pyrosim as pyrosim
import pybullet as p
from sensor import SENSOR
from motor import MOTOR


class ROBOT:
    def __init__(self):
        pyrosim.Prepare_To_Simulate("body.urdf")
        self.robot = p.loadURDF("body.urdf")
        self.sensors = {}
        self.motors = {}

        self.Prepare_To_Sense()
        self.Prepare_To_Act()

    def Prepare_To_Sense(self):
        for linkName in pyrosim.linkNamesToIndices:
            self.sensors[linkName] = SENSOR(linkName)

    def Sense(self, t):
        for s in self.sensors.values():
            s.Get_Value(t)

    def Prepare_To_Act(self):
        for jointName in pyrosim.jointNamesToIndices:
            self.motors[jointName] = MOTOR(jointName)

    def Act(self, t):
        for m in self.motors.values():
            m.Set_Value(t, self.robot)
