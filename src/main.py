from src.brown_movement import BrownMovement
from src.plot import Plot


def lam2():
    plot = Plot()
    x, y = BrownMovement(tmp=10, p=1e4, r=1e-6, N=250).act()
    plot.draw(x, y)
    x, y = BrownMovement(tmp=293.15, p=1e4, r=1e-8, N=1000).act()
    plot.draw(x, y)
    x, y = BrownMovement(tmp=293.15, p=1e4, r=1e-8, N=250).act()
    plot.draw(x, y)
    x, y = BrownMovement(tmp=220.5, p=1e4, r=1e-6, N=250).act()
    plot.draw(x, y)
    x, y = BrownMovement(tmp=293.15, p=1e4, r=1e-11, N=250).act()
    plot.draw(x, y)


if __name__ == "__main__":
    lam2()