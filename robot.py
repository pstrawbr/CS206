import pyrosim.pyrosim as pyrosim
import pybullet as p
from sensor import SENSOR
from motor import MOTOR
from pyrosim.neuralNetwork import NEURAL_NETWORK
import os


class ROBOT:
    def __init__(self, solutionID):
        pyrosim.Prepare_To_Simulate("body.urdf")
        self.robot = p.loadURDF("body.urdf")
        self.sensors = {}
        self.motors = {}
        self.nn = NEURAL_NETWORK("brain" + str(solutionID) + ".nndf")

        self.Prepare_To_Sense()
        self.Prepare_To_Act()
        os.system("del brain" + str(solutionID) + ".nndf")

    def Prepare_To_Sense(self):
        for linkName in pyrosim.linkNamesToIndices:
            self.sensors[linkName] = SENSOR(linkName)

    def Sense(self, t):
        for s in self.sensors.values():
            s.Get_Value(t)

    def Prepare_To_Act(self):
        for jointName in pyrosim.jointNamesToIndices:
            self.motors[jointName] = MOTOR(jointName)

    def Act(self):
        for neuronName in self.nn.Get_Neuron_Names():
            if self.nn.Is_Motor_Neuron(neuronName):
                desiredAngle = self.nn.Get_Value_Of(neuronName)
                for m in self.motors.values():
                    m.Set_Value(desiredAngle, self.robot)

    def Think(self):
        self.nn.Update()

    def Get_Fitness(self, solutionID):
        stateOfLinkZero = p.getLinkState(self.robot,0)
        positionOfLinkZero = stateOfLinkZero[0]
        xCoordinateOfLinkZero = positionOfLinkZero[0]
        f = open("tmp" + str(solutionID) + ".txt", "w")
        f.write(str(xCoordinateOfLinkZero))
        f.close()
        os.rename("tmp" + str(solutionID) + ".txt", "fitness" + str(solutionID) + ".txt")
