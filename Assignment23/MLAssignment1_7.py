import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def Dataf():
   data = {'Name': ['Amit' , 'Sagar', 'Pooja'],
          'Math' : [85 , 90, 87],
          'Science' : [92 , 88, 80],
          'English' : [80 , 85 ,82]}
   
   df = pd.DataFrame(data)
   df['Total'] = [250, 263, 249]

   plt.figure(figsize= (10,5))
   sns.barplot(data = df ,x = 'Name', y = 'Total')
   plt.title("Students and their marks")
   plt.xlabel("Name")
   plt.ylabel("Total")
   plt.grid(True)
   plt.show()

def main():
   Dataf()

if __name__ == "__main__":
   main()   