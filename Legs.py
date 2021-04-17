import constants as c
import numpy


class Legs:
    def __init__(self):
        self.num = c.numberOfLegs

        self.upperLegsJointPositions = []
        self.upperLegsJointAxis = []

        self.upperLegsPositions = []
        self.upperLegsSize = []

        self.lowerLegsJointPositions = []

        degreesBetween = 360.0/self.num

        torsoJointZ = 1
        jointAxisZ = 0
        Zsize = 0.2
        angle = 0

        for i in range(self.num):
            x = numpy.cos(numpy.radians(angle)) / 2
            y = numpy.sin(numpy.radians(angle)) / 2

            angle += degreesBetween
            if 0.001 > x > 0 or -0.001 < x < 0:
                x = 0
            if 0.001 > y > 0 or -0.001 < y < 0:
                y = 0
            self.upperLegsJointPositions.append([x,y,torsoJointZ])
            self.lowerLegsJointPositions.append([x*2,y*2,jointAxisZ])

            if x != 0:
                Xaxis = 0
                Xsize = 1
            else:
                Xaxis = 1
                Xsize = 0.2
            if y != 0:
                Yaxis = 0
                Ysize = 1
            else:
                Yaxis = 1
                Ysize = 0.2
            self.upperLegsJointAxis.append([Xaxis,Yaxis,jointAxisZ])

            self.upperLegsPositions.append([x,y,0])
            self.upperLegsSize.append([Xsize,Ysize,Zsize])
