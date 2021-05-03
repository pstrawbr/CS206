import numpy

torsoSides = 4

gravityX = 0
gravityY = 0
gravityZ = -9.8

iterations = 1000
maxForce = 100
sleepTime = 1 / 2400

amplitude = numpy.pi / 3
frequency = 10
phaseOffset = 0

length = 1
height = 1

numberOfGenerations = 5
populationSize = 5

motorJointRange = 0.6

numberOfLegs = 4
torsoWidth = (numberOfLegs - 2 / 2) / 3

numSensorNeurons = numberOfLegs
numMotorNeurons = numberOfLegs * 2

orientation = 0
