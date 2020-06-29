import numpy as np
import matplotlib.pyplot as plt
import spectrumDataConverter as sdc
import scipy as sp
from scipy.optimize import curve_fit

df = sdc.spectrum("csvSpectrum.txt")

x = np.array(df[1])
y = np.array(df[2])

plt.plot(x, y)
plt.show()

def planckFunc(T, v):
    B = ((2*(sp.constants.Planck)*(v**3) / ((sp.constants.c)**2)) * (1 / ((sp.constants.e)**(((sp.constants.Planck) * v) / (sp.constants.k) * T) - 1)))
    return B


x = np.array([float(i) for i in x])
y = np.array([float(i) for i in y])


params = curve_fit(planckFunc, x, y)
print(params)
[T] = params[0]

