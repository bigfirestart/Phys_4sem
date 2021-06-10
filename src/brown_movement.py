import math
import random
import numpy as np
from enum import Enum


class Constants(Enum):
    k = 1.38e-23


class BrownMovement:
    def __init__(self, t, p, r, N):
        self.tmp, self.p, self.r, self.N, self.sum_l = [t, p, r, N, 0]
        self.x, self.y = [0], [0]
        center = (Constants.k.value * self.tmp) / (math.sqrt(2) * math.pi * ((self.r * 2) ** 2) * self.p)
        self.lmd_array = np.random.normal(center, 0.01e-16, N + 1)

    def __calculate_next_step(self, iter: int):
        change = 1
        if random.random() > 0.5:
            change = -1
        angle = math.acos(2 * random.random() - 1)
        x0 = self.x[len(self.x) - 1]
        y0 = self.y[len(self.y) - 1]
        self.x.append(x0 + self.lmd_array[iter] * math.cos(angle))
        self.y.append(y0 + self.lmd_array[iter] * math.sin(angle) * change)

    def act(self):
        iter = 0
        while iter <= self.N:
            self.__calculate_next_step(iter=iter)
            self.sum_l += self.lmd_array[iter]
            iter += 1

        print("Средняя длина =", self.sum_l / self.N)
        print("Постоянная Больцмана =", self.sum_l / self.N / self.tmp *
              (math.sqrt(2) * math.pi * ((self.r * 2) ** 2) * self.p))
        print("---------------------------")
        return self.x, self.y
