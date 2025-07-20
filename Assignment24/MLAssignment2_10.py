import pandas as pd
from sklearn.preprocessing import MinMaxScaler
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def Dataf():
   df = pd.read_csv('data.csv')
   
   sns.boxplot(x = 'Name'  , y = 'English' , data = df)
   plt.title("English boxplot")
   plt.show()

def main():
    Dataf()

if __name__ == "__main__":
    main()    