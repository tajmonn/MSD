import numpy as np
import matplotlib.pyplot as plt
from sympy import Function, dsolve, Eq, symbols, plot
from scipy.integrate import odeint
from os import system
plt.style.use('ggplot')
system('cls')

# Dane:
t = symbols('t')            # czas
N = Function('N')           # funkcja N
r = 0.75                    # współczynnik reprodukcji
K = 2                       # pojemność środowiska
N_0 = [K/40, 3/4*K, K+2]    # wielkości początkowe populacji

"""# Model Verhulsta: dN_dt = rN(1-N/K)"""
verhulst = Eq(N(t).diff(t), r*N(t)*(1- N(t)/K))

# Tworzenie wykresu dla 3 róznych wielkości początkowych (sympy)
sol1 = dsolve(verhulst, ics={N(0): N_0[0]})
sol2 = dsolve(verhulst, ics={N(0): N_0[1]})
sol3 = dsolve(verhulst, ics={N(0): N_0[2]})

p1 = plot(sol1.rhs, sol2.rhs, sol3.rhs, (t, 0, 12), yaxis=(0,4), legend=True, show=False, title='sympy: Model Verhulsta', xlabel='czas $t$', ylabel ='liczebnosc populacji')
p1[0].line_color = 'red'
p1[1].line_color = 'blue'
p1[2].line_color = 'purple'
p1.show()

# Tworzenie tablic z wynikami (get_points() daje dla 65 kroków)
time1, so1 = p1[0].get_points()
time2, so2 = p1[1].get_points()
time3, so3 = p1[2].get_points()

def s_ver(x, t):
    """Model Verhulsta dla scipy"""
    return x*r*(1-x/K)

T1 = len(time1)   # Liczba kroków
T2 = len(time2)
T3 = len(time3)

# Tworzenie wykresu dla 3 róznych wielkości początkowych (scipy)
time1 = np.linspace(0, 12, T1)
time2 = np.linspace(0, 12, T2)
time3 = np.linspace(0, 12, T3)
X = odeint(s_ver, np.asarray(N_0[0]), time1, full_output=True)[0]
Y = odeint(s_ver, np.asarray(N_0[1]), time2, full_output=True)[0]
Z = odeint(s_ver, np.asarray(N_0[2]), time3, full_output=True)[0]
plt.plot(time1, X, label='N(0) = K/40')
plt.plot(time2, Y, label='N(0) = 3/4*K')
plt.plot(time3, Z, label='N(0) = K+2')
plt.legend()
plt.title('scipy: Model Verhulsta')
plt.xlabel('czas $t$')
plt.ylabel('liczebnosc populacji')
plt.show()


# Obliczanie błędów
MAE_1, MAE_2, MAE_3 = 0, 0, 0
MSE_1, MSE_2, MSE_3 = 0, 0 , 0
error1, error2, error3 = [], [], []

for i in range(T1):
    MAE_1 += abs(X[i] - so1[i])/T1
    MSE_1 += ((X[i] - so1[i])**2)/T1
    error1.append((X[i] - so1[i])/T1)

for i in range(T2):
    MAE_2 += abs(Y[i] - so2[i])/T2
    MSE_2 += ((Y[i] - so2[i])**2)/T2
    error2.append((Y[i] - so2[i])/T2)

for i in range(T3):
    MAE_3 += abs(Z[i] - so3[i])/T3
    MSE_3 += ((Z[i] - so3[i])**2)/T3
    error3.append((Z[i] - so3[i])/T3)


print("Bledy bezwzgledne:")
print(f"K/40  (krok: {12/T1}): {MAE_1[0]}\n3/4*K (krok: {12/T2}): {MAE_2[0]}\nK+2   (krok: {12/T3}): {MAE_3[0]}")
print("\nBledy kwadratowe:")
print(f"K/40  (krok: {12/T1}): {MSE_1[0]}\n3/4*K (krok: {12/T2}): {MSE_2[0]}\nK+2   (krok: {12/T3}): {MSE_3[0]}\n")

# Tworzenie wykresu dla błędów
plt.plot(time1, error1, label='N(0) = K/40')
plt.plot(time2, error2, label='N(0) = 3/4*K')
plt.plot(time3, error3, label='N(0) = K+2')
plt.legend()
plt.title(f'bledy')
plt.xlabel('czas $t$')
plt.ylabel('scipy - sympy')
plt.show()

