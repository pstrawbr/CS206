from parallelHillClimber import PARALELL_HILL_CLIMBER
import constants as c
import os


loop = True

if loop:
    a_b = [0] # , 1, 2
    legNums = [8] # 4,6 ,
    os.system("del bestFitness.txt")
    #names = ["oct"] # "quad", "hex",
    names = ['']
    #for orient in orients:
        #f = open("bestFitness.txt", "a")
        #f.write("Orientation: " + str(orient) + "\n")
        #f.close()
    for pos in a_b:
        c.numberOfLegs = legNums[pos]
        c.orientation = 0
        if c.numberOfLegs == 4:
            torsoWidth = 1
        else:
            torsoWidth = (c.numberOfLegs - 2 / 2) / 4
        c.numSensorNeurons = legNums[pos]
        c.numMotorNeurons = legNums[pos] * 2

        phc = PARALELL_HILL_CLIMBER(names[pos], loop)
        phc.Evolve()
        phc.Show_Best()

else:
    phc = PARALELL_HILL_CLIMBER("", loop)
    phc.Evolve()
    phc.Show_Best()
