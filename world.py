import pybullet as p


class WORLD:
    def __init__(self, ID):
        self.planeId = p.loadURDF("plane.urdf")
        self.world = p.loadSDF("world"+str(ID)+".sdf")
