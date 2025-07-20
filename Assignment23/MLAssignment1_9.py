import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

def Dataf():
   data2 = {'Name': ['Amit' , 'Sagar', 'Pooja'],
          'Math' : [np.nan , 76, 88],
          'Science' : [91 , np.nan, 85]}
   
   df2 = pd.DataFrame(data2)

   df2[['Math', 'Science']] = df2[['Math', 'Science']].fillna(df2[['Math', 'Science']].mean())

   print("DataFrame after Filling Missing Values with Column Mean ")
   print(df2)
   
def main():
   Dataf()

if __name__ == "__main__":
   main()   