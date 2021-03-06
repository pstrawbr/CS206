import pybullet as p


class WORLD:
    def __init__(self):
        self.planeId = p.loadURDF("plane.urdf")
        self.world = p.loadSDF("world.sdf")
        self.robot = p.loadURDF("body.urdf")
