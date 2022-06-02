import numpy as np
import matplotlib.pyplot as plt
import matplotlib
from scipy.integrate import odeint
matplotlib.style.use('ggplot')


sigma = 10
beta = 8/3
rho = 28


def simulate(x0, y0, z0, T, dt):
    n = int(T/dt)
    t = np.zeros(n + 1)
    x = np.zeros(n + 1)
    y = np.zeros(n + 1)
    z = np.zeros(n + 1)
    x[0] = x0
    y[0] = y0
    z[0] = z0
    t[0] = 0
    for k in range(n):
        t[k+1] = t[k] + dt
        x[k+1] = x[k] + dt * dx_dt(x[k], y[k], z[k])
        y[k+1] = y[k] + dt * dy_dt(x[k], y[k], z[k])
        z[k+1] = z[k] + dt * dz_dt(x[k], y[k], z[k])
    return x, y, z, t


def dx_dt(x, y, z):
    return sigma*(y-x)


def dy_dt(x, y, z):
    return x*(rho-z) - y
    

def dz_dt(x, y, z):
    return x*y - beta*z


def dxyz_dt(xyz, t):
    x, y, z = xyz
    return dx_dt(x,y,z), dy_dt(x,y,z), dz_dt(x,y,z)


# metoda Eulera

fig, ax = plt.subplots(nrows=3, ncols=3, figsize=(15,9))
plt.suptitle("Układ Lorenza zamodelowany przy pomocy metody Eulera")
for index, dt in enumerate([0.03, 0.02, 0.01]):   
    x, y, z, t = simulate(x0=1, y0=1, z0=1, T=25, dt=dt)
    ax[index][0].plot(x, y)
    ax[index][1].plot(x, z)
    ax[index][2].plot(y, z)
    ax[index][1].set_title(f'dt = {dt}')
    plt.plot()

    # obliczanie błędu
    n = int(25/dt)
    X, infodict = odeint(dxyz_dt, np.asarray([1, 1, 1]), np.linspace(0, 25, n), full_output=True)
    print(infodict['message'])
    odeint_x, odeint_y, odeint_z = X.T
    error = round(abs(sum(x) - sum(odeint_x) + sum(y) - sum(odeint_y) + sum(z) - sum(odeint_z)) / (3*n), 5)
    print(f'Średni błąd aproksymacyjny dla dt = {dt} wynosi {error}')

plt.show()

x, y, z, t = simulate(x0=1, y0=1, z0=1, T=25, dt=0.002)
fig = plt.figure()
ax = fig.add_subplot(projection='3d')
plt.suptitle('Układ Lorenza zamodelowany przy pomocy metody Eulera\ndt = 0.002')
ax.plot(x,y,z)
plt.show()


# scipy.integrate.odeint

dt = 0.002
t_max = 25
n = int(t_max/0.002)

t = np.linspace(0, t_max, n)
x0 = np.asarray([1, 1, 1])

X, infodict = odeint(dxyz_dt, x0, t, full_output=True)
print(infodict['message'])

x, y, z = X.T
fig, ax = plt.subplots(nrows=3, ncols=1, figsize=(5,9))
plt.suptitle(f'Układ Lorenza zamodelowany przy pomocy odeint\ndt = {dt}')
ax[0].plot(x, y)
ax[1].plot(x, z)
ax[2].plot(y, z)
plt.show()


fig = plt.figure()
ax = fig.add_subplot(projection='3d')
plt.suptitle(f'Układ Lorenza zamodelowany przy pomocy odeint\ndt = {dt}')
ax.plot(x,y,z)
plt.show()