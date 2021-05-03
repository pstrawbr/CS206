from solution import SOLUTION
import constants as c
import copy, os


class PARALELL_HILL_CLIMBER:
    def __init__(self):
        os.system("del brain*.nndf")
        os.system("del fitness*.txt")
        os.system("del body*.urdf")
        os.system("del world*.sdf")
        self.parents = {}
        self.nextAvailableID = 0
        for i in range(c.populationSize):
            self.parents[i] = SOLUTION(self.nextAvailableID)
            self.nextAvailableID += 1

    def Evolve(self):
        self.Evaluate(self.parents, mode="DIRECT")

        for currentGeneration in range(c.numberOfGenerations):
            self.Evolve_For_One_Generation(mode="DIRECT")

    def Evolve_For_One_Generation(self, mode):
        self.Spawn()
        self.Mutate()
        self.Evaluate(self.children, mode)
        self.Print()
        self.Select()

    def Spawn(self):
        self.children = {}
        for key in self.parents:
            self.children[key] = copy.deepcopy(self.parents[key])
            self.children[key].Set_ID(self.nextAvailableID)
            self.nextAvailableID += 1

    def Mutate(self):
        for key in self.children:
            self.children[key].Mutate()

    def Evaluate(self, solutions, mode):
        for key in solutions:
            solutions[key].Start_Simulation(mode=mode)
        for key in solutions:
            solutions[key].Wait_For_Simulation_To_End()

    def Select(self):
        for key in self.children:
            if self.parents[key].fitness > self.children[key].fitness:
                self.parents[key] = self.children[key]

    def Print(self):
        print('\n----------------------------------------------------------')
        for key in self.parents:
            print("Parent:", self.parents[key].fitness, "\tChild:", self.children[key].fitness)
        print('----------------------------------------------------------\n')

    def Show_Best(self, loop):
        lowest = self.parents[0].fitness
        temp = self.parents[0]
        for key in self.parents:
            if self.parents[key].fitness < lowest:
                lowest = self.parents[key].fitness
                temp = self.parents[key]
        if not loop:
            temp.Start_Simulation(mode="GUI")

        if loop:
            f = open("bestFitness.txt", "a")
            f.write(str(c.numberOfLegs) + ": " + str(temp.fitness) + "\n")
            f.close()
