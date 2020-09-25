import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import spectrumDataConverter as sdc
import pandas as pd


def calculateNewWavelength(wlObserved, redshift):
    wlEmitted = wlObserved / (1 + redshift)
    return wlEmitted

def shiftWl(file, redshift):
    d = sdc.spectrum(file)
    dShifted = {"Wavelength": (calculateNewWavelength(d["Wavelength"], redshift)),
                "BestFit": d["BestFit"]}
    dShifted = pd.DataFrame(dShifted, columns = ["Wavelength","BestFit"])
    return dShifted