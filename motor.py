import pyrosim.pyrosim as pyrosim
import pybullet as p
import constants as c
import numpy


class MOTOR:
    def __init__(self, jointName):
        self.jointName = jointName

        self.Prepare_To_Act()

    def Prepare_To_Act(self):
        self.amplitude = c.amplitudeBack
        self.frequency = c.frequencyBack
        self.offset = c.phaseOffsetBack
        if self.jointName == 'Torso_BackLeg':
            self.frequency = 2

        self.motorValues = (self.amplitude * numpy.sin(self.frequency * numpy.linspace(-numpy.pi, numpy.pi, c.iterations) + self.offset))

    def Set_Value(self, t, robot):
        pyrosim.Set_Motor_For_Joint(
            bodyIndex=robot,
            jointName=self.jointName,
            controlMode=p.POSITION_CONTROL,
            targetPosition=self.motorValues[t],
            maxForce=c.maxForce)

    def Save_Values(self):
        numpy.save("data/" + self.jointName + "TargetAngles.npy", self.motorValues)
