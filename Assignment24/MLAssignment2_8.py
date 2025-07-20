import pandas as pd
from sklearn.preprocessing import MinMaxScaler
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def Dataf():
   df = pd.read_csv('data.csv')

   plt.hist(df["Math"], bins = 10, color = "skyblue", edgecolor = "black" ) 
   plt.ylabel("Math")
   plt.xlabel("Marks")
   plt.title("Histogram for Math marks")
   plt.show()

def main():
    Dataf()

if __name__ == "__main__":
    main()    