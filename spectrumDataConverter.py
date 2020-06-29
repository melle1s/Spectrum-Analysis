import pandas as pd

def spectrum(file):
    data = file

    df = pd.read_csv(data)

    df1 = df[["Wavelength","BestFit"]]

    #df1.set_index("Wavelength", inplace = True)

    return df1

