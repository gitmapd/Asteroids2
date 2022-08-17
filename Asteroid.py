import numpy as numpy

from Vector3D import Vector3D

class Asteroid:
    def __init__(self, pos: Vector3D, vel: Vector3D, m):
        self.pos = pos
        self.vel = vel
        self.m  = m
    def __repr__(self):
        return f'Asteroid({self.pos!r},{self.m!r})'

    def move(self,t):
        self.pos += self.vel * t

class Comet(Asteroid):
    def __init__(self, pos: Vector3D, vel: Vector3D):
        self.q = 1.6e-19
        self.m = 9.11e-31
        super(Comet,self).__init__(pos,vel,self.m)
