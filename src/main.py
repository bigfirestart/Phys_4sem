from src.atom_model import AtomModel
from src.brown_movement import BrownMovement
from src.plot import Plot


def lab1():
    atom = AtomModel(n=3, l=2, m=1)
    atom.plot_slice()
    atom.z_axis_plot()

    atom = AtomModel(n=3, l=1, m=0)
    atom.plot_slice()
    atom.z_axis_plot()


def lab2():
    plot = Plot()
    x, y = BrownMovement(t=10, p=1e4, r=1e-6, N=250).act()
    plot.draw(x, y)
    x, y = BrownMovement(t=293.15, p=1e4, r=1e-8, N=1000).act()
    plot.draw(x, y)
    x, y = BrownMovement(t=293.15, p=1e4, r=1e-8, N=250).act()
    plot.draw(x, y)
    x, y = BrownMovement(t=220.5, p=1e4, r=1e-6, N=250).act()
    plot.draw(x, y)
    x, y = BrownMovement(t=293.15, p=1e4, r=1e-11, N=250).act()
    plot.draw(x, y)


if __name__ == "__main__":
    lab1()