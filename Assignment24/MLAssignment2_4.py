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
   
   sagarMarks = df[df['Name'] == 'Sagar'][['Math', 'Science', 'English']].iloc[0]

   SMI  = sagarMarks.index
   size = sagarMarks.values

   plt.pie(size , labels= SMI )
   plt.title("Marks of sagar pie chart")
   plt.show()

def main():
    Dataf()

if __name__ == "__main__":
    main()    