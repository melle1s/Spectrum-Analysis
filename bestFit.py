import numpy as np
import matplotlib.pyplot as plt
import redshiftAccount as rsa
import spectrumDataConverter as sdc
import scipy as sp
import pandas as pd
from scipy import constants
from scipy.optimize import curve_fit

h = constants.h
c = constants.c
k = constants.k
#df = sdc.spectrum("csvSpectrum1.txt")    
df = rsa.shiftWl("SDSS J115709.94-002113.1", 0.0002895092)                     # Getting the data (using pandas in another .py file)
print(df)
def wien_model(wlPeak):                                     # The wien displacement law can be used to approximate the temperature of the star
    return ((sp.constants.Wien) / wlPeak)

def planck(wav, T):                                         # This is the correct Planck's law formula
    a = 2.0*h*c**2
    b = h*c/(wav*k*T)
    intensity = a/ ( (wav**5) * (np.exp(b) - 1.0) )
    return intensity / 1000 / 10**9                         # Converting to correct units (kW · sr⁻¹ · m⁻² · nm⁻¹) * π


#fluxPeak = df["Flux"].max()                                 # Gets the maximum value of bestfit
bestFitPeak = df["BestFit"].max()
#wlPeak = df["Wavelength"][pd.Index(df["Flux"]).get_loc(fluxPeak)]       # Finds the wavelength at which bestFit peaks
wlPeakBF = df["Wavelength"][pd.Index(df["BestFit"]).get_loc(bestFitPeak)]
wlPeakBF = wlPeakBF * 10**-10
#wlPeak = wlPeak * 10**-10                                   # Converts the wavelength from Å to m (correct unit for Wien displacement law)

#approx_T = wien_model(wlPeak)                               # Gets the approximate temperature of the star (I've used this for reference only)
approx_T_BF = wien_model(wlPeakBF)

wavelengths = df["Wavelength"] * 10**-10                    # Converts wavelength data to m, instead of Å

init_guess = approx_T_BF
 
#fit = curve_fit(planck, wavelengths, (df["Flux"] / constants.pi), init_guess)         # Fitting the Planck's law model to the observed data
fit2 = curve_fit(planck, wavelengths, (df["BestFit"] / constants.pi), init_guess)

#ans = fit[0]
ans2 = fit2[0]

#intensities = planck(wavelengths, ans)                      # Calculating y-axis
intensities2 = planck(wavelengths, ans2)     
#plt.plot(wavelengths * 10**10, intensities * constants.pi, "r-", label = str(ans) + " K")      # Plotting the fitted data
plt.plot(wavelengths * 10**10, intensities2 * constants.pi, "k-", label = str(ans2) + " K")
#plt.plot(wavelengths * 10**10, planck(wavelengths, approx_T) * constants.pi, "g-", label = str(np.round(approx_T)) + " K")
plt.plot(wavelengths * 10**10, planck(wavelengths, approx_T_BF) * constants.pi, "y-", label = str(np.round(approx_T_BF)) + " K")
#plt.plot(wavelengths * 10**10, df["Flux"], "b-", label = "Observed Flux")
plt.plot(wavelengths * 10**10, df["BestFit"], "m-", label = "BestFit")
plt.legend()
plt.savefig("curvefit.png")
plt.show()

