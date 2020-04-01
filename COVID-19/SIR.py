import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

# Total population, N.
N = 11690000
# Initial number of infected and recovered individuals, I0 and R0.
I0, R0 = 100, 0
# Everyone else, S0, is susceptible to infection initially.
S0 = N - I0 - R0
# Contact rate, beta, and mean recovery rate, gamma, (in 1/days).
beta, gamma = 3/14, 1/14
print("R0 = "+ str(beta/gamma))
# A grid of time points (in days)
tStop = 300
t = np.linspace(0, tStop, tStop*10)

qStart = 0
isq = False

# The SIR model differential equations.
def deriv(y, t, N, beta, gamma):
    S, I, R = y
    beta, gamma = 3/14, 1/14
    if(t%2<1 and t>60):
        beta = .5/14
    elif(t>60):
        beta = 2/14

    dSdt = -beta * S * I / N
    dIdt = beta * S * I / N - gamma * I

    dRdt = gamma * I
    if(dRdt<0):
        dRdt = 0
    return dSdt, dIdt, dRdt

# Initial conditions vector
y0 = S0, I0, R0
# Integrate the SIR equations over the time grid, t.
ret = odeint(deriv, y0, t, args=(N, beta, gamma))
S, I, R = ret.T

# Plot the data on three separate curves for S(t), I(t) and R(t)
fig = plt.figure(facecolor='w')
ax = fig.add_subplot(111)
ax.plot(t, S/1000000, 'b', alpha=0.5, lw=2, label='Susceptible')
ax.plot(t, I/1000000, 'r', alpha=0.5, lw=2, label='Infected')
ax.plot(t, R/1000000, 'g', alpha=0.5, lw=2, label='Recovered with immunity')
ax.plot(t, R*0.04/1000000, 'black', alpha=0.5, lw=2, label='Death')
ax.plot(t, I*0.25/1000000, 'purple', alpha=0.5, lw=2, label='Critical Condition')
ax.set_xlabel('Time (days)')
ax.set_ylabel('Number cases (millions)')
ax.set_ylim(0,12)
ax.yaxis.set_tick_params(length=0)
ax.xaxis.set_tick_params(length=0)
ax.grid(b=True, which='major', c='w', lw=2, ls='-')
legend = ax.legend()
legend.get_frame().set_alpha(0.5)
for spine in ('top', 'right', 'bottom', 'left'):
    ax.spines[spine].set_visible(False)
plt.show()

plt.plot(S,I)
plt.show()
