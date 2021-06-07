import math
import random
from enum import Enum


class Constants(Enum):
    k = 1.38e-23


class BrownMovement:
    def __init__(self, tmp, p, r, N):
        self.tmp, self.p, self.r, self.N, self.sum_l = [tmp, p, r, N, 0]
        self.x, self.y = [0], [0]

    @property
    def lmd(self):
        return 0 if self.tmp == 0 else (Constants.k.value * self.tmp) / (
                    math.sqrt(2) * math.pi * ((self.r * 2) ** 2) * self.p) + (
                                                   random.random() * 0.4e-16 - random.random() * 0.45e-16)

    def calculate_next_step(self):
        change = 1
        if random.random() > 0.5:
            change = -1
        angle = math.acos(2 * random.random() - 1)
        x0 = self.x[len(self.x) - 1]
        y0 = self.y[len(self.y) - 1]
        self.x.append(x0 + self.lmd * math.cos(angle))
        self.y.append(y0 + self.lmd * math.sin(angle) * change)

    def act(self):
        iter = 0
        while iter <= self.N:
            self.calculate_next_step()
            self.sum_l += self.lmd
            print(self.x[len(self.x) - 1], self.y[len(self.y) - 1], "Длина = ", self.sum_l)
            iter += 1

        print("Средняя длина =", self.sum_l / self.N)
        print("Постоянная Больцмана =", self.sum_l / self.N / self.tmp *
              (math.sqrt(2) * math.pi * ((self.r * 2) ** 2) * self.p))
        return self.x, self.y
