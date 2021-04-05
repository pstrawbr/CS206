import numpy
import pyrosim.pyrosim as pyrosim
import constants as c
import random
import os, time


class SOLUTION:
    def __init__(self, myID):
        self.weights = (numpy.random.rand(3,2) * 2) - 1
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
        randomColumn = random.randint(0,2)
        randomRow = random.randint(0,1)
        self.weights[randomColumn][randomRow] = (random.random() * 2) - 1

    def Set_ID(self, nextAvailableID):
        self.myID = nextAvailableID + 1

    def Create_Body(self):
        pyrosim.Start_URDF("body.urdf")
        x = 1.5
        y = 0
        z = 1.5
        pyrosim.Send_Cube(name="Torso", pos=[x, y, z], size=[c.length, c.width, c.height])

        pyrosim.Send_Joint(name="Torso_BackLeg", parent="Torso", child="BackLeg", type="revolute", position="1 0 1")
        pyrosim.Send_Joint(name="Torso_FrontLeg", parent="Torso", child="FrontLeg", type="revolute", position="2 0 1")
        z = - 0.5
        x = 0.5
        pyrosim.Send_Cube(name="BackLeg", pos=[-x, y, z], size=[c.length, c.width, c.height])
        pyrosim.Send_Cube(name="FrontLeg", pos=[x, y, z], size=[c.length, c.width, c.height])

        pyrosim.End()

    def Create_Brain(self):
        pyrosim.Start_NeuralNetwork("brain" + str(self.myID) + ".nndf")
        pyrosim.Send_Sensor_Neuron(name=0, linkName="Torso")
        pyrosim.Send_Sensor_Neuron(name=1, linkName="BackLeg")
        pyrosim.Send_Sensor_Neuron(name=2, linkName="FrontLeg")
        pyrosim.Send_Motor_Neuron(name=3, jointName="Torso_BackLeg")
        pyrosim.Send_Motor_Neuron(name=4, jointName="Torso_FrontLeg")

        for currentColumn in range(3):
            for currentRow in range(2):
                pyrosim.Send_Synapse(sourceNeuronName=currentColumn,
                                     targetNeuronName=currentRow+3,
                                     weight=self.weights[currentColumn][currentRow])
        pyrosim.End()

    def Create_World(self):
        pyrosim.Start_SDF("world.sdf")
        x = 2
        y = 2
        z = 0.5
        pyrosim.Send_Cube(name="Box", pos=[x, y, z], size=[c.length, c.width, c.height])

        pyrosim.End()
