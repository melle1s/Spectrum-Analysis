import numpy as np
from scipy.optimize import curve_fit
import scipy as sp
import pandas as pd
import matplotlib.pyplot as plt
import spectrumDataConverter as sdc

h = 6.626e-34
c = 3.0e+8
k = 1.38e-23


def planck(wav, T):
    a = 2.0*h*c**2
    b = h*c/(wav*k*T)
    intensity = a/ ( (wav**5) * (np.exp(b) - 1.0) )
    return intensity




def model(wl, T):
   B = ((2*(sp.constants.Planck)*(sp.constants.c**2) / ((wl)**5)) * (1 / ((sp.constants.e)**(((sp.constants.Planck) * sp.constants.c) / (wl * (sp.constants.k) * T))) - 1))
   #B = ((2 * sp.constants.h * (sp.constants.c**2)) / (wl**5)) * (1 / (sp.constants.e**((sp.constants.h * sp.constants.c) / (wl * sp.constants.k * T)) - 1))
   return B

def wien_model(wl_peak):
    return ((sp.constants.Wien) / wl_peak)

d = sdc.spectrum("csvSpectrum.txt")

fit = curve_fit(planck, d["Wavelength"] * 10**10, (d["BestFit"]))
print(fit)
ans, cov = fit

fit_T = ans

print(fit_T)

y1 = []
y2 = []



for wl in d["Wavelength"]:
    y1.append(planck(wl * 10**-10, 4000))
    y2.append(planck(wl * 10**-10, 2000))

plt.plot(d["Wavelength"], planck(d["Wavelength"], fit_T), "black", label = "curve_fit")
plt.plot(d["Wavelength"], y1, "r", label = "4000 K")
plt.plot(d["Wavelength"], y2, "b", label = "2000 K")
plt.plot(d["Wavelength"], d["BestFit"] * 10**10, "g", label = "Data")
plt.legend()
plt.show()

print(wien_model(9.9))