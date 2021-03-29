from solution import SOLUTION
import constants as c
import copy


class HILL_CLIMBER:
    def __init__(self):
        self.parent = SOLUTION()

    def Evolve(self):
        self.parent.Evaluate(mode="DIRECT")
        for currentGeneration in range(c.numberOfGenerations):
            if currentGeneration == 0:
                self.Evolve_For_One_Generation(mode = "GUI")
            else:
                self.Evolve_For_One_Generation(mode="DIRECT")

    def Evolve_For_One_Generation(self, mode):
        self.Spawn()
        self.Mutate()
        self.child.Evaluate(mode)
        self.Print()
        self.Select()

    def Spawn(self):
        self.child = copy.deepcopy(self.parent)

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
        self.parent.Evaluate(mode="GUI")
