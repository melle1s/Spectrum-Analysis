import scipy as sp
import numpy as np
import matplotlib.pyplot as plt
import matplotlib 
from scipy import constants

h = constants.h
c = constants.c
k = constants.k


def planck(wav, T):
    a = 2.0*h*c**2
    b = h*c/(wav*k*T)
    intensity = a/ ( (wav**5) * (np.exp(b) - 1.0) )
    return intensity

wavelengths = np.arange(1e-9, 10e-6, 1e-9) 

# intensity at 4000K, 5000K, 6000K, 7000K
intensity4000 = planck(wavelengths, 4000.)
intensity5000 = planck(wavelengths, 5000.)
intensity6000 = planck(wavelengths, 6000.)
intensity7000 = planck(wavelengths, 7000.)


plt.plot(wavelengths*1e9, intensity4000, 'r-', label = "4000 K") 
 #plot intensity4000 versus wavelength in nm as a red line
plt.plot(wavelengths*1e9, intensity5000, 'g-', label = "5000 K") # 5000K green line
plt.plot(wavelengths*1e9, intensity6000, 'b-', label = "6000 K") # 6000K blue line
plt.plot(wavelengths*1e9, intensity7000, 'k-', label = "7000 K") # 7000K black line
plt.legend()
# show the plot
plt.savefig("correct.png")
plt.show()
