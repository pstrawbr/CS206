import constants as c


class Legs:
    def __init__(self):
        self.upperLegsJointPositions = []
        self.upperLegsJointAxis = []
        self.upperLegsPositions = []
        self.upperLegsSize = []
        self.lowerLegsJointPositions = []

        self.buildLeftAndRight()
        if c.numberOfLegs >= c.torsoSides:
            self.buildFrontAndBack()

    def buildLeftAndRight(self):
        Xpos = 0
        Ypos = c.torsoWidth / 2
        Zpos = 1

        Xaxis = 1
        Yaxis = 0
        Zaxis = 0

        Xsize = 0.2
        Ysize = 1
        Zsize = 0.2

        for i in range(2):
            if Ypos > 0:
                YjointPos = Ysize
            else:
                YjointPos = -Ysize
            self.upperLegsJointPositions.append([Xpos, Ypos, Zpos])
            self.lowerLegsJointPositions.append([Xpos, YjointPos, Zaxis])
            self.upperLegsJointAxis.append([Xaxis, Yaxis, Zaxis])
            self.upperLegsPositions.append([Xpos, YjointPos / 2, Zpos - 1])
            self.upperLegsSize.append([Xsize, Ysize, Zsize])

            Ypos -= c.torsoWidth

    def buildFrontAndBack(self):
        numYLegs = int((c.numberOfLegs - 2) / 2)  # NUMBER ON EACH SIDE (6 Legs = 2)
        spaceBetween = c.torsoWidth / (numYLegs + 1)

        Xsize = 1
        Ysize = 0.2
        Zsize = 0.2

        Xaxis = 0
        Yaxis = 1
        Zaxis = 0

        if numYLegs % 2 == 0:
            Ypos = (spaceBetween / 2) + (numYLegs / 2) * - spaceBetween
        else:
            Ypos = ((numYLegs - 1) / 2) * - spaceBetween

        Xpos = 0.5
        Zpos = 1

        for i in range(numYLegs):
            self.upperLegsJointPositions.append([Xpos, Ypos, Zpos])
            self.lowerLegsJointPositions.append([Xpos * 2, 0, Zaxis])
            self.upperLegsJointAxis.append([Xaxis, Yaxis, Zaxis])
            self.upperLegsPositions.append([Xpos, 0, Zpos - 1])
            self.upperLegsSize.append([Xsize, Ysize, Zsize])
            Ypos += spaceBetween

        if numYLegs % 2 == 0:
            Ypos = (spaceBetween / 2) + (numYLegs / 2) * - spaceBetween
        else:
            Ypos = ((numYLegs - 1) / 2) * - spaceBetween
        Xpos = -0.5

        for i in range(numYLegs):
            self.upperLegsJointPositions.append([Xpos, Ypos, Zpos])
            self.lowerLegsJointPositions.append([Xpos * 2, 0, Zaxis])
            self.upperLegsJointAxis.append([Xaxis, Yaxis, Zaxis])
            self.upperLegsPositions.append([Xpos, 0, Zpos - 1])
            self.upperLegsSize.append([Xsize, Ysize, Zsize])
            Ypos += spaceBetween
