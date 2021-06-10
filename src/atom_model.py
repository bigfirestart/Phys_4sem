import numpy as np
import math
from scipy.special import sph_harm
import scipy.special
import matplotlib.pyplot as plt


class AtomModel:
    def __init__(self, n, l, m):
        self.n, self.l, self.m = [n, l, m]
        self.d = 0.2
        self.min = -20
        self.max = 20
        self.wf = None
        self.x = np.arange(self.min, self.max, self.d)
        self.y = np.arange(self.min, self.max, self.d)
        self.z = np.arange(self.min, self.max, self.d)
        self.X, self.Y, self.Z = np.meshgrid(self.x, self.y, self.z)
        self.__calculate_wave_function()

    def __calculate_wave_function(self):
        R = np.sqrt(self.X ** 2 + self.Y ** 2 + self.Z ** 2)
        Theta = np.arccos(self.Z / R)
        Phi = np.arctan2(self.Y, self.X)
        a = 0.5291 * 10e-10
        rho = 2. * R / self.n
        s_harm = sph_harm(self.m, self.l, Phi, Theta)
        l_poly = scipy.special.genlaguerre(self.n - self.l - 1, 2 * self.l + 1)(rho)

        prefactor = np.sqrt((2. / self.n / a) ** 3 * math.factorial(self.n - self.l - 1) / (2. * self.n * math.factorial(self.n + self.l)))
        wf = prefactor * np.exp(-rho / 2.) * rho ** self.l * s_harm * l_poly
        self.wf = np.nan_to_num(wf)

    def plot_slice(self):
        data = abs(self.wf) ** 2
        fig, ax = plt.subplots()
        plt.subplots_adjust(left=0.15, bottom=0.15)
        im = plt.imshow(data[int((0 - self.min) / self.d), :, :], vmin=0, vmax=np.max(data), extent=[self.min, self.max, self.min, self.max])
        plt.colorbar()
        ax.set_title(
            "Hydrogen Orbital xz Slice (y=0): n=" + str(self.n) + ", l=" + str(self.l) + ", m=" + str(self.m))

        plt.show()

    def z_axis_plot(self):
        data = abs(self.wf) ** 2

        plt.figure()
        plt.plot(self.z, data[int(len(self.z) / 2), int(len(self.z) / 2), :])
        plt.title("$|\psi_{nlm}|^2$(x=0,y=0,z): n=" + str(self.n) + ", l=" + str(self.l) + ", m=" + str(self.m))
        plt.xlabel('z')
        plt.ylabel("$|\psi_{nlm}|^2$")
        plt.show()