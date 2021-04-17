import numpy
import pyrosim.pyrosim as pyrosim
import constants as c
import random
import os, time


class SOLUTION:
    def __init__(self, myID):
        self.weights = (numpy.random.rand(c.numSensorNeurons, c.numMotorNeurons) * 2) - 1
        self.myID = myID

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

        pyrosim.Send_Joint(name="Torso_FrontLeg", parent="Torso", child="FrontLeg", type="revolute", position="0 0.5 1", jointAxis="1 0 0")
        pyrosim.Send_Cube(name="FrontLeg", pos=[0, .5, 0], size=[.2, 1, .2])

        pyrosim.Send_Joint(name="Torso_BackLeg", parent="Torso", child="BackLeg", type="revolute", position="0 -0.5 1", jointAxis="1 0 0")
        pyrosim.Send_Cube(name="BackLeg", pos=[0, -.5, 0], size=[.2, 1, .2])

        pyrosim.Send_Joint(name="Torso_LeftLeg", parent="Torso", child="LeftLeg", type="revolute", position="-0.5 0 1", jointAxis="0 1 0")
        pyrosim.Send_Cube(name="LeftLeg", pos=[-.5, 0, 0], size=[1, 0.2, .2])

        pyrosim.Send_Joint(name="Torso_RightLeg", parent="Torso", child="RightLeg", type="revolute", position="0.5 0 1", jointAxis="0 1 0")
        pyrosim.Send_Cube(name="RightLeg", pos=[.5, 0, 0], size=[1, 0.2, .2])

        pyrosim.Send_Joint(name="FrontLeg_FrontLowerLeg", parent="FrontLeg", child="FrontLowerLeg", type="revolute", position="0 1 0", jointAxis="1 0 0")
        pyrosim.Send_Cube(name="FrontLowerLeg", pos=[0, 0, -0.5], size=[0.2, 0.2, 1])

        pyrosim.Send_Joint(name="BackLeg_BackLowerLeg", parent="BackLeg", child="BackLowerLeg", type="revolute", position="0 -1 0", jointAxis="1 0 0")
        pyrosim.Send_Cube(name="BackLowerLeg", pos=[0, 0, -0.5], size=[0.2, 0.2, 1])

        pyrosim.Send_Joint(name="LeftLeg_LeftLowerLeg", parent="LeftLeg", child="LeftLowerLeg", type="revolute", position="-1 0 0", jointAxis="0 1 0")
        pyrosim.Send_Cube(name="LeftLowerLeg", pos=[0, 0, -0.5], size=[0.2, 0.2, 1])

        pyrosim.Send_Joint(name="RightLeg_RightLowerLeg", parent="RightLeg", child="RightLowerLeg", type="revolute", position="1 0 0", jointAxis="0 1 0")
        pyrosim.Send_Cube(name="RightLowerLeg", pos=[0, 0, -0.5], size=[0.2, 0.2, 1])

        pyrosim.End()

    def Create_Brain(self):
        pyrosim.Start_NeuralNetwork("brain" + str(self.myID) + ".nndf")
        pyrosim.Send_Sensor_Neuron(name=0, linkName="FrontLowerLeg")
        pyrosim.Send_Sensor_Neuron(name=1, linkName="BackLowerLeg")
        pyrosim.Send_Sensor_Neuron(name=2, linkName="LeftLowerLeg")
        pyrosim.Send_Sensor_Neuron(name=3, linkName="RightLowerLeg")

        pyrosim.Send_Motor_Neuron(name=4, jointName="Torso_FrontLeg")
        pyrosim.Send_Motor_Neuron(name=5, jointName="Torso_BackLeg")
        pyrosim.Send_Motor_Neuron(name=6, jointName="Torso_LeftLeg")
        pyrosim.Send_Motor_Neuron(name=7, jointName="Torso_RightLeg")
        pyrosim.Send_Motor_Neuron(name=8, jointName="FrontLeg_FrontLowerLeg")
        pyrosim.Send_Motor_Neuron(name=9, jointName="BackLeg_BackLowerLeg")
        pyrosim.Send_Motor_Neuron(name=10, jointName="LeftLeg_LeftLowerLeg")
        pyrosim.Send_Motor_Neuron(name=11, jointName="RightLeg_RightLowerLeg")

        for currentRow in range(c.numSensorNeurons):
            for currentColumn in range(c.numMotorNeurons):
                pyrosim.Send_Synapse(sourceNeuronName=currentRow,
                                     targetNeuronName=currentColumn + c.numSensorNeurons,
                                     weight=self.weights[currentRow][currentColumn])

        pyrosim.End()

    def Create_World(self):
        pyrosim.Start_SDF("world"+str(self.myID)+".sdf")
        x = 2
        y = 2
        z = 0.5
        pyrosim.Send_Cube(name="Box", pos=[x, y, z], size=[c.length, c.width, c.height])

        pyrosim.End()
