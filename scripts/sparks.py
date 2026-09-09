import pygame
import math

class Spark:
    def __init__(self, pos, angle, speed):
        self.pos = list(pos)
        self.angle = angle
        self.speed = speed

    def update(self):
        self.pos[0] += math.cos(self.angle) * self.speed
        self.pos[1] += math.sin(self.angle) * self.speed

        self.speed = max(0, self.speed - 0.1)
        return not self.speed