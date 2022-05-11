import numpy as np
import matplotlib.pyplot as plt
from os import system
from scipy.integrate import odeint


####    Metoda Lotki-Volterra   ####

def LV_p(xy, t):
    """Funkcja metody Lotki-Volterra dla scipy"""
    x, y = xy
    return (a-b*y)*x, (c*x-d)*y

def Lor_p(xyz, t):
    """Funkcja metody Lorenza dla scipy"""
    x, y, z = xyz
    return alfa*(y-x), x * (gamma - z) - y, x * y - beta * z

def LV(dx_dt, dy_dt, x0, y0, T, dt):
    """Funkcja naśladująca metodę Eulera dla układu Lotkki-Volterry"""
    n = int(T/dt)
    t = np.zeros(n+1)
    x = np.zeros(n+1)
    y = np.zeros(n+1)
    t[0] = 0
    x[0] = x0
    y[0] = y0
    for k in range(n):
        t[k+1] = t[k] + dt
        x[k+1] = x[k] + dt * dx_dt(x[k], y[k])
        y[k+1] = y[k] + dt * dy_dt(x[k], y[k]) 
    return t, x, y

def LV_x(x, y):
    """Funkcja dx/dt dla układu Lotki-Volterry"""
    return (a-b*y)*x

def LV_y(x, y):
    """Funkcja dy/dt dla układu Lotki-Volterry"""
    return (c*x-d)*y


#   dane początkowe
a      = 1.2   # częstość narodzin ofiar
b      = 0.6   # częstość umierania ofiar
LV_x0  = 2     # populacja początkowa ofiar
c      = 0.3   # częstość narodzin drapieżników 
d      = 0.8   # częstość umierania drapieżników
LV_y0  = 1     # populacja początkowa drapieżników

#   dane do wykresów
LV_dts = [0.3, 0.1, 0.01]   # Skoki dla kolejnych wykresów (dt)
LV_T   = 25                 # Okres dla wykresu

answears = ["Dla metody Lotki-Volterra:"]  # tablica na odpowiedzi 

"""Tworzenie 3 wykresów dla układu Lotki-Volterra + błąd"""
fig,(ax1, ax2, ax3) = plt.subplots(3) 
figs = [ax1, ax2, ax3]
for n in range(3):
    t, x, y = LV(LV_x, LV_y, LV_x0, LV_y0, LV_T, LV_dts[n])
    figs[n].plot(t, x, label="Ofiary")
    figs[n].plot(t, y, label="Drapieżniki")
    figs[n].set_title(f"dt = {LV_dts[n]}")
    figs[n].legend()
    figs[n].set_ylabel('Liczba osobników')

    # Obliczanie błędu ze scipy
    X, infodict = odeint(LV_p, np.asarray([LV_x0, LV_y0]), np.linspace(0, LV_T, int(LV_T/LV_dts[n])), full_output=True)
    new_x, new_y = X.T
    summa = abs(sum(new_x) + sum(new_y) - sum(x) - sum(y))/(2*int(LV_T/LV_dts[n])) 
    answears.append(f"Dla dt = \033[1m{LV_dts[n]}\033[0m, bezwzględny średni błąd wynosi = \033[1m{summa}\033[0m")

figs[2].set_xlabel('Czas')
plt.show()



#####   Metoda Lorenza   #####

def Lor(x0, y0, z0, T, dt):
    """Funkcja naśladująca metodę Eulera dla układu Lorenza"""
    n = int(T/dt)
    t = np.zeros(n+1)
    x = np.zeros(n+1)
    y = np.zeros(n+1)
    z = np.zeros(n+1)
    t[0], x[0], y[0], z[0] = 0, x0, y0, z0  # dane początkowe
    for k in range(n):
        t[k+1] = t[k] + dt
        x[k+1] = x[k] + dt * Lor_x(x[k], y[k], z[k])
        y[k+1] = y[k] + dt * Lor_y(x[k], y[k], z[k])
        z[k+1] = z[k] + dt * Lor_z(x[k], y[k], z[k])
    return t, x, y, z

def Lor_x(x, y, z):
    """Funkcja dx/dt dla układu Lorenza"""
    return alfa*(y-x)

def Lor_y(x, y, z):
    """Funkcja dy/dt dla układu Lorenza"""
    return x * (gamma - z) - y

def Lor_z(x, y, z):
    """Funkcja dz/dt dla układu Lorenza"""
    return x * y - beta * z


#   dane początkowe
Lor_x0  = 1     # x początkowe
Lor_y0  = 1     # y początkowe
Lor_z0  = 1     # z początkowe
alfa    = 10    # stała alfa
beta    = 8/3   # stała beta
gamma   = 28    # stała gamma

#   dane do wykresów
Lor_dts = [0.03, 0.02, 0.01]     # Skoki dla kolejnych wykresów (dt)
Lor_T = 25                       # Okres dla wykresu
fig,((ax1, ax2, ax3),(ax4, ax5, ax6),(ax7, ax8, ax9)) = plt.subplots(3, 3, figsize=(15,9))     
figs = [[ax1, ax2, ax3], [ax4, ax5, ax6], [ax7, ax8, ax9]]    
colors = ['orange', 'blue', 'green']  # Kolory wykresów

#   Estetyczna odpowiedz ciąg dalszy
answears.append("")
answears.append("Dla metody Lorenza:")

"""Tworzenie 9 wykresów dla układu Lorenza + błąd"""
for m in range(3):
    t, x, y, z = Lor(Lor_x0, Lor_y0, Lor_z0, Lor_T, Lor_dts[m])
    figs[m][0].plot(x, y, colors[0], label='y(x)')
    figs[m][1].plot(x, z, colors[1], label='z(x)')
    figs[m][2].plot(y, z, colors[2], label='z(y)')
    # zamiast opisywac lub nazywać wykresy daje legende dla lepszej czytelności
    figs[m][0].legend()
    figs[m][1].legend()
    figs[m][2].legend()
    figs[m][1].set_title(f"dt = {Lor_dts[m]}")
    # w przypadku pierwszej funkcji dostajemy dużo nan'ów więc zamieniam je na zera, dla łatwiejszego liczenia błędu
    x = np.nan_to_num(x)
    y = np.nan_to_num(y)
    z = np.nan_to_num(z)
    
    # Obliczanie błędu ze scipy
    X, infodict = odeint(Lor_p, np.asarray([Lor_x0, Lor_y0, Lor_z0]), np.linspace(0, Lor_T, int(Lor_T/Lor_dts[m])), full_output=True)
    new_x, new_y, new_z = X.T
    summa = abs(sum(new_x) + sum(new_y) + sum(new_z) - sum(x) - sum(y) - sum(z))/(3*int(Lor_T/Lor_dts[m])) 
    answears.append(f"Dla dt = \033[1m{Lor_dts[m]}\033[0m, bezwzględny średni błąd wynosi = \033[1m{summa}\033[0m")

plt.show()


"""Tworzenie 3 trójwymiarowych wykresów dla układu Lorenza"""
fig = plt.figure(figsize=(10,10))
for m in range(3):
    t, x, y, z = Lor(Lor_x0, Lor_y0, Lor_z0, Lor_T, Lor_dts[m])
    ax = fig.add_subplot(2, 2, m+1, projection='3d')
    ax.plot3D(x, y, z, colors[m])
    ax.set_title(f"dt = {Lor_dts[m]}")\
    # set bo set_coślabel nie działa dla subplotów?
    ax.set(xlabel='X', ylabel='Y', zlabel='Z')

plt.show()


# Estetyczna odpowiedź (za dużo warningów wyskakuje)
system('cls')
for i in answears:
    print(i)