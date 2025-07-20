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
 
   scale = MinMaxScaler()
   N  = ['Math']
   df[N] = scale.fit_transform(df[N])

   print("The normalize data is " , df[N])

def main():
    Dataf()

if __name__ == "__main__":
    main()    
