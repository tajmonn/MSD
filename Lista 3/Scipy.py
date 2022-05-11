from scipy.integrate import odeint
import numpy as np
import matplotlib.pyplot as plt
from os import system

def LV(xy, t):
    """Funkcja metody Lotki-Volterra dla scipy"""
    x, y = xy
    return (a-b*y)*x, (c*x-d)*y

def Lor(xyz, t):
    """Funkcja metody Lorenza dla scipy"""
    x, y, z = xyz
    return alfa*(y-x), x * (gamma - z) - y, x * y - beta * z


#   dane początkowe dla metody L-V
a      = 1.2   # częstość narodzin ofiar
b      = 0.6   # częstość umierania ofiar
LV_x0  = 2     # populacja początkowa ofiar
c      = 0.3   # częstość narodzin drapieżników 
d      = 0.8   # częstość umierania drapieżników
LV_y0  = 1     # populacja początkowa drapieżników
LV_T   = 25    # okres trwania procesu
LV_dt  = 0.002 # długość skoku

"""Tworzenie wykresu dla metody L-V"""
t = np.linspace(0, LV_T, int(LV_T/LV_dt))
X, infodict = odeint(LV, np.asarray([LV_x0, LV_y0]), t, full_output=True)
infodict['message']
x, y = X.T
fig, ax = plt.subplots()
ax.plot(t, x, 'red', label='ofiary')
ax.plot(t, y, 'blue', label='drapieżniki')
ax.set_xlabel('Liczba osobników')
ax.set_ylabel('Czas')
ax.legend()
ax.grid(True)
fig.tight_layout()
plt.show()


#   dane początkowe dla metody Lorenza
Lor_x0  = 1     # x początkowe
Lor_y0  = 1     # y początkowe
Lor_z0  = 1     # z początkowe
alfa    = 10    # stała alfa
beta    = 8/3   # stała beta
gamma   = 28    # stała gamma
Lor_T   = 25    # okres trwania procesu
Lor_dt  = 0.002 # długość skoku

"""Tworzenie wykresów dla metody Lorenza"""
t = np.linspace(0, Lor_T, int(Lor_T/Lor_dt))
X, infodict = odeint(Lor, np.asarray([Lor_x0, Lor_y0, Lor_z0]), t, full_output=True)
infodict['message']
x, y, z = X.T
fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2,2, figsize=(10,10))
ax1.plot(x, y, 'orange')
ax1.set(xlabel='X', ylabel='Y')
ax2.set_visible(False)
ax3.plot(x, z, 'blue')
ax3.set(xlabel='X', ylabel='Z')
ax4.plot(y, z, 'green')
ax4.set(xlabel='Y', ylabel='Z')
fig.tight_layout()
plt.show()

"""Tworzenie trójwymiarowego wykresu dla układu Lorenza"""
fig = plt.figure(figsize=(10,10))
ax = fig.add_subplot(projection='3d')
ax.plot3D(x, y, z, 'green')
ax.set_title(f"dt = 0.002")
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
plt.show()

system('cls')


