from parallelHillClimber import PARALELL_HILL_CLIMBER
import constants as c
import os


loop = False

if loop:
    legNums = [4, 6, 8, 10, 12, 14]
    os.system("del bestFitness.txt")
    divs = [3, 6]

    for div in divs:
        f = open("bestFitness.txt", "a")
        f.write(str(div) + "\n")
        f.close()
        for num in legNums:
            c.numberOfLegs = num
            c.orientation = 0
            c.torsoWidth = (num - 2 / 2) / div
            c.numSensorNeurons = num
            c.numMotorNeurons = num * 2

            phc = PARALELL_HILL_CLIMBER()
            phc.Evolve()
            phc.Show_Best(loop)

else:
    phc = PARALELL_HILL_CLIMBER()
    phc.Evolve()
    phc.Show_Best(loop)
