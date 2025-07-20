import pandas as pd
import numpy as np

def Dataf():
   data = {'Name': ['Amit' , 'Sagar', 'Pooja'],
          'Math' : [85 , 90, 87],
          'Science' : [85 , 88, 80],
          'English' : [80 , 85 ,82]}
   
   df = pd.DataFrame(data)

   df['Total'] = [250, 263, 249]
   
   df.to_csv("data.csv")

def main():
    Dataf()

if __name__ == "__main__":
    main()    