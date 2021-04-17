import numpy
import pyrosim.pyrosim as pyrosim
import constants as c
import random
import os, time
from Legs import Legs


class SOLUTION:
    def __init__(self, myID):
        self.weights = (numpy.random.rand(c.numSensorNeurons, c.numMotorNeurons) * 2) - 1
        self.myID = myID
        self.legs = Legs()

    def Start_Simulation(self, mode):
        self.Create_World()
        self.Create_Body()
        self.Create_Brain()
        os.system("start /B py simulate.py " + mode + " " + str(self.myID))

    def Wait_For_Simulation_To_End(self):
        while not os.path.exists("fitness" + str(self.myID) + ".txt"):
            time.sleep(0.01)
        f = open("fitness" + str(self.myID) + ".txt", "r")
        self.fitness = float(f.read())
        f.close()
        os.system("del fitness" + str(self.myID) + ".txt")


    def Mutate(self):
        randomColumn = random.randint(0, c.numMotorNeurons - 1)
        randomRow = random.randint(0, c.numSensorNeurons - 1)
        self.weights[randomRow][randomColumn] = (random.random() * 2) - 1

    def Set_ID(self, nextAvailableID):
        self.myID = nextAvailableID + 1

    def Create_Body(self):
        pyrosim.Start_URDF("body"+str(self.myID)+".urdf")

        pyrosim.Send_Cube(name="Torso", pos=[0, 0, 1], size=[c.length, c.width, c.height])

        for i in range(c.numberOfLegs):
            pyrosim.Send_Joint(name="Torso_"+str(i), parent="Torso", child=str(i), type="revolute",
                               position=str(self.legs.upperLegsJointPositions[i][0]) + " " + str(
                                   self.legs.upperLegsJointPositions[i][1]) + " " + str(
                                   self.legs.upperLegsJointPositions[i][2]),
                               jointAxis=str(self.legs.upperLegsJointAxis[i][0]) + " " + str(
                                   self.legs.upperLegsJointAxis[i][1]) + " " + str(self.legs.upperLegsJointAxis[i][2]))
            pyrosim.Send_Cube(name=str(i),
                              pos=self.legs.upperLegsPositions[i],
                              size=self.legs.upperLegsSize[i])

            pyrosim.Send_Joint(name=str(i)+"_Lower" + str(i), parent=str(i), child="Lower" + str(i), type="revolute",
                               position=str(self.legs.lowerLegsJointPositions[i][0]) + " " + str(
                                   self.legs.lowerLegsJointPositions[i][1]) + " " + str(
                                   self.legs.lowerLegsJointPositions[i][2]),
                               jointAxis=str(self.legs.upperLegsJointAxis[i][0]) + " " + str(
                                   self.legs.upperLegsJointAxis[i][1]) + " " + str(self.legs.upperLegsJointAxis[i][2]))
            pyrosim.Send_Cube(name="Lower" + str(i), pos=[0, 0, -0.5], size=[0.2, 0.2, 1])

        pyrosim.End()

    def Create_Brain(self):
        pyrosim.Start_NeuralNetwork("brain" + str(self.myID) + ".nndf")

        for i in range(c.numberOfLegs):
            pyrosim.Send_Sensor_Neuron(name=i, linkName="Lower"+str(i))
        for i in range(c.numberOfLegs, c.numberOfLegs * 2):
            pyrosim.Send_Motor_Neuron(name=i, jointName="Torso_"+str(i))
        for i in range(c.numberOfLegs * 2, c.numberOfLegs * 3):
            pyrosim.Send_Motor_Neuron(name=i, jointName=str(i) + "_Lower" + str(i))

        for currentRow in range(c.numSensorNeurons):
            for currentColumn in range(c.numMotorNeurons):
                pyrosim.Send_Synapse(sourceNeuronName=currentRow,
                                     targetNeuronName=currentColumn + c.numSensorNeurons,
                                     weight=self.weights[currentRow][currentColumn])

        pyrosim.End()

    def Create_World(self):
        pyrosim.Start_SDF("world"+str(self.myID)+".sdf")
        pyrosim.End()
