import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

x_data = np.array([40,50,60,70,80,160])
y_data = np.array([30859.375,30156.25,29531.25,29062.5,28750,28066.406])
params = np.array([1,1])





#fit = np.polyfit(np.log(x_data), y_data)
#print(fit)

def funcinv(x, a, b, c):
    # The inverse funciton
    return b + a/(x - c)

# popt - optimal params after least squares
# pcov - estimated covariance of popt
# for more information see docs https://docs.scipy.org/doc/scipy/reference/generated/scipy.optimize.curve_fit.html
popt, pcov = curve_fit(funcinv, x_data, y_data)
print(popt)
print(pcov)

# r squared calculation 
# see https://stackoverflow.com/questions/19189362/getting-the-r-squared-value-using-curve-fit
residuals = y_data - funcinv(x_data, *popt)
ss_res = np.sum(residuals**2)
ss_tot = np.sum((y_data-np.mean(y_data))**2)
r_squared = 1 - (ss_res / ss_tot)
print("R^2 : " + str(r_squared))


tStop = 300
t = np.linspace(30, tStop, tStop*10)


# Plot the data on three separate curves for S(t), I(t) and R(t)
plt.plot(x_data,y_data, 'ro', t, funcinv(t, *popt), "b")

plt.show()