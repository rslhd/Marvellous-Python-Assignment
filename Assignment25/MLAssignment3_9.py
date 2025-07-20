import pandas as pd
import numpy as np

def data():
    data = {'Marks':[45, 67, 88, 38, 76]}
    df = pd.DataFrame(data)

    df['Marks'] = np.where(df['Marks'] <= 50, 'Fail', df['Marks'])

    print("The new dataframe is ", df)

def main():
    data()

if __name__ == "__main__":
    main()       