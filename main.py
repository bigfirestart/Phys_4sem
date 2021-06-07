import matplotlib.pyplot as plt

from brown_movement import BrownMovement


def lam2():
    x, y = BrownMovement(tmp=10, p=1e4, r=1e-6, N=250).act()
    plt.plot(x, y, marker='o')
    plt.grid(True)
    plt.show()


if __name__ == "__main__":
    lam2()

