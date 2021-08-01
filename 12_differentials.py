import matplotlib.pyplot as plt

#%% Predators and prey

def plot_population_change(rabbit_start, fox_start, days, steps):
    # hourly change
    n_rabbit = [rabbit_start]
    n_fox = [fox_start]
    hours = days * steps

    for i in range(0, hours):
        delta_rabbit = (n_rabbit[-1] * 0.05 - 0.0002 * n_fox[-1] * n_rabbit[-1])/steps
        delta_fox = (0.0001 * n_fox[-1] * n_rabbit[-1] - n_fox[-1] * 0.1)/steps
        n_rabbit.append(n_rabbit[-1] + delta_rabbit)  # setting the calculated as new base
        n_fox.append(n_fox[-1] + delta_fox)  # setting the calculated as new base

    plt.figure()
    plt.plot(n_rabbit, label='rabbits')
    plt.plot(n_fox, label='foxes')
    plt.legend()


#%% Lateral inhibition
notch1 = notch2 = delta2 = 1
delta1 = 0.99
a = 0.01
b = 100
k = 2
h = 2
time = 50
dt = 0.2
steps = int(time/dt)

for i in range(steps):
    # cell 1
    notch_change1 = (delta2**k) / (a + delta2**k) - notch1
    delta_change1 = 1 / (1 + b * notch1 ** h) - delta1
    # cell 2
    notch_change2 = (delta1**k) / (a + delta1**k) - notch2
    delta_change2 = 1 / (1 + b * notch2 ** h) - delta2

    # apply changes
    notch1 += notch_change1 * dt
    notch2 += notch_change2 * dt
    delta1 += delta_change1 * dt
    delta2 += delta_change2 * dt

print('Delta Cell 1: {:.8f}'.format(delta1))
print('Delta Cell 2: {:.8f}'.format(delta2))
print('Notch Cell 1: {:.8f}'.format(notch1))
print('Notch Cell 2: {:.8f}'.format(notch2))

#%% with functions

notch1 = notch2 = delta2 = 1
delta1 = 0.99
a = 0.01
b = 100
k = 2
h = 2
time = 50
dt = 0.2
steps = int(time/dt)

def notch(x):
    fx = (x**k) / (a+x**k)
    return fx

def delta(x):
    gx = 1/(1+b*x**h)
    return gx

for i in range(steps):
    # cell 1
    notch_change1 = notch(delta2) - notch1
    delta_change1 = delta(notch1) - delta1
    # cell 2
    notch_change2 = notch(delta1) - notch2
    delta_change2 = delta(notch2) - delta2

    # apply changes
    notch1 += notch_change1 * dt
    notch2 += notch_change2 * dt
    delta1 += delta_change1 * dt
    delta2 += delta_change2 * dt

print('Delta Cell 1: {:.8f}'.format(delta1))
print('Delta Cell 2: {:.8f}'.format(delta2))
print('Notch Cell 1: {:.8f}'.format(notch1))
print('Notch Cell 2: {:.8f}'.format(notch2))


#%% with numpy array (saves all timesteps)

import numpy as np

def rhs(f):
    a, b = 0.01, 100
    N1, D1, N2, D2 = f[0], f[1], f[2], f[3]
    dN1 = D2 ** 2 / (a + D2 ** 2) - N1
    dD1 = 1 / (1 + b * N1 ** 2) - D1
    dN2 = D1 ** 2 / (a + D1 ** 2) - N2
    dD2 = 1 / (1 + b * N2 ** 2) - D2
    return np.array([dN1, dD1, dN2, dD2])

t = np.linspace(0, 50, 101)
f = np.zeros(shape=(len(t), 4))

# initial conditions
f[0, 0], f[0, 1], f[0, 2], f[0, 3] = 1, 0.99, 1, 1

for n in range(len(t) - 1):
    dt = t[n + 1] - t[n]
    df = dt * rhs(f[n])
    df = dt * rhs(f[n] + df / 2)  # mid-point method
    f[n + 1] = f[n] + df

print('N1 D1', f[-1, :2])
print('N2 D2', f[-1, 2:])

#%% Solving ODEs analytically

# x(t) = x0 * exp(c*t)
c = 0.03
x0 = 1000
t = 20

x_t = x0 * np.exp(c*t)
print(int(x_t))

for i in range(steps):
    x0 += (c * x0) * 0.05
print(x0)

# compare analytical with numerical (Euler method)
t = 20
dt = [0.05, 0.1, 0.2]
c = 0.03
for step in dt:
    steps = int(t/step)
    x = 1000
    x_t = x * np.exp(c * t)
    for i in range(steps):
        x += (c*x) * step

    print('Delta_t stepsize {}: {:.2f}'.format(step, x-x_t))

# mid-point method
t = 20
dt = [0.05, 0.1, 0.2]
c = 0.03
for step in dt:
    steps = int(t/step)
    x = 1000
    x_t = x * np.exp(c * t)
    for i in range(steps):
        x_mid = x + 0.5*(c*x) * step
        x = x + (c*x_mid) * step

    print('Delta_t stepsize {}: {:.4f}'.format(step, x-x_t))

