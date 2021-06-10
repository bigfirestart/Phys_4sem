from enum import Enum
import matplotlib.pyplot as plt


class Plot:
    def __init__(self):
        self.iter = 0
        self.colors = ['red', 'royalblue', 'green', 'darkviolet', 'orangered']

    def draw(self, x, y):
        plt.plot(x, y, marker='o', color=self.colors[self.iter])
        plt.grid(True)
        plt.show()
        self.iter += 1
