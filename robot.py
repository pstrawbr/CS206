import pyrosim.pyrosim as pyrosim
from sensor import SENSOR
from motor import MOTOR


class ROBOT:
    def __init__(self):
        self.motors = {}

        self.Prepare_To_Sense()

    def Prepare_To_Sense(self):
        self.sensors = {}
        for linkName in pyrosim.linkNamesToIndices:
            print(linkName) #TODO remove this after fixing linkNamesToIndices
            self.sensors[linkName] = SENSOR(linkName)
