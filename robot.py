import pyrosim.pyrosim as pyrosim
import pybullet as p
from sensor import SENSOR
from motor import MOTOR
from pyrosim.neuralNetwork import NEURAL_NETWORK
import os
import constants as c


class ROBOT:
    def __init__(self, solutionID):
        pyrosim.Prepare_To_Simulate("body"+str(solutionID)+".urdf")
        self.robot = p.loadURDF("body"+str(solutionID)+".urdf")
        self.sensors = {}
        self.motors = {}
        self.nn = NEURAL_NETWORK("brain" + str(solutionID) + ".nndf")

        self.Prepare_To_Sense()
        self.Prepare_To_Act()
        os.system("del brain" + str(solutionID) + ".nndf")
        os.system("del body" + str(solutionID) + ".urdf")
        os.system("del world" + str(solutionID) + ".sdf")

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
                desiredAngle = self.nn.Get_Value_Of(neuronName) * c.motorJointRange
                for m in self.motors.values():
                    m.Set_Value(desiredAngle, self.robot)

    def Think(self):
        self.nn.Update()

    def Get_Fitness(self, solutionID):
        basePositionAndOrientation = p.getBasePositionAndOrientation(self.robot)
        basePosition = basePositionAndOrientation[0]
        xPosition = basePosition[0]
        f = open("tmp" + str(solutionID) + ".txt", "w")
        f.write(str(xPosition))
        f.close()
        os.rename("tmp" + str(solutionID) + ".txt", "fitness" + str(solutionID) + ".txt")
