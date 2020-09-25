import pandas as pd

def spectrum(file):
    data = file

    df = pd.read_csv(data)

    df1 = df[["Wavelength", "BestFit", "Flux"]]

    return df1

