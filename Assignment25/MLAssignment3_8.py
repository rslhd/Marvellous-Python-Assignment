import pandas as pd
import numpy as np

def data():
    data = {'Marks': [85, np.nan, 90, np.nan, 95]}

    df = pd.DataFrame(data)

    df['MarksInter'] = df['Marks'].interpolate()

    print("The interpolated DataFrame ", df)

def main():
    data()

if __name__ == "__main__":
    main()   