import numpy as numpy

from Vector3D import Vector3D

class Bullet:
    def __init__(self, pos: Vector3D, vel: Vector3D, size: float, color: float):
        self.pos     = pos
        self.vel     = vel
        self.size    = size
        self.color   = color


