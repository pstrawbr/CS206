from solution import SOLUTION
import constants as c
import copy


class PARALLEL_HILL_CLIMBER:
    def __init__(self):
        self.parents = {}
        self.nextAvailableID = 0
        for i in range(c.populationSize):
            self.parents[i] = SOLUTION(self.nextAvailableID)
            self.nextAvailableID += 1

    def Evolve(self):
        for key in self.parents:
            self.parents[key].Evaluate(mode="GUI")
        # self.parent.Evaluate(mode="DIRECT")
        # for currentGeneration in range(c.numberOfGenerations):
        #     if currentGeneration == 0:
        #         self.Evolve_For_One_Generation(mode = "GUI")
        #     else:
        #         self.Evolve_For_One_Generation(mode="DIRECT")

    def Evolve_For_One_Generation(self, mode):
        self.Spawn()
        self.Mutate()
        self.child.Evaluate(mode)
        self.Print()
        self.Select()

    def Spawn(self):
        self.child = copy.deepcopy(self.parent)
        self.child.Set_ID()
        self.nextAvailableID += 1

    def Mutate(self):
        self.child.Mutate()

    def Select(self):
        if self.parent.fitness > self.child.fitness:
            self.parent = self.child

    def Print(self):
        print('\n----------------------------------------------------------')
        print("Parent:", self.parent.fitness, "\tChild:", self.child.fitness)
        print('----------------------------------------------------------\n')

    def Show_Best(self):
        pass
        # self.parent.Evaluate(mode="GUI")
