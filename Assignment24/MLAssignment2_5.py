import pandas as pd
from sklearn.preprocessing import MinMaxScaler
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def Dataf():
   data = {'Name': ['Amit' , 'Sagar', 'Pooja'],
          'Math' : [85 , 90, 87],
          'Science' : [85 , 88, 80],
          'English' : [80 , 85 ,82]}
   
   df = pd.DataFrame(data)
   print("Data is ", df)

   df['Total'] = [250, 263, 249]
   df['Status'] = np.where(df['Total'] >= 250, 'Pass', 'Fail')

   print("The new data with status column:", df.head())

def main():
    Dataf()

if __name__ == "__main__":
    main()    