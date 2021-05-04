from parallelHillClimber import PARALELL_HILL_CLIMBER
import constants as c
import os


loop = False

if loop:
    legNums = [4, 6, 8, 10, 12, 14]
    os.system("del bestFitness.txt")
    orients = [0, 1]

    for orient in orients:
        f = open("bestFitness.txt", "a")
        f.write("Orientation: " + str(orient) + "\n")
        f.close()
        for num in legNums:
            c.numberOfLegs = num
            c.orientation = 0
            if c.numberOfLegs == 4:
                torsoWidth = 1
            else:
                torsoWidth = (c.numberOfLegs - 2 / 2) / 4
            c.numSensorNeurons = num
            c.numMotorNeurons = num * 2

            phc = PARALELL_HILL_CLIMBER()
            phc.Evolve()
            phc.Show_Best(loop)

else:
    phc = PARALELL_HILL_CLIMBER()
    phc.Evolve()
    phc.Show_Best(loop)
