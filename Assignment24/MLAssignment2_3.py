import pandas as pd
from sklearn.preprocessing import MinMaxScaler
import numpy as np

def Dataf():
   data = {'Name': ['Amit' , 'Sagar', 'Pooja'],
          'Math' : [85 , 90, 87],
          'Science' : [85 , 88, 80],
          'English' : [80 , 85 ,82]}
   
   df = pd.DataFrame(data)
   print("Data is ", df)
   
   df['Gender'] = ['Male' , 'Male', 'Female']
   print("The gender column is " , df.head())

   df['Gender'] = df['Gender'].map({'Male' : 0 , 'Female' : 1})
   print("The encoded gender column is ", df.head())

   groupedWithMarks = df.groupby('Gender')[['Math', 'Science', 'English']].mean()
   print("The average marks are ", groupedWithMarks)

def main():
    Dataf()

if __name__ == "__main__":
    main()    