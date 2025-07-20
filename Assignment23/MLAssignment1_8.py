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

   Amit = df[df['Name'] == 'Amit'][['Math', 'Science', 'English']].iloc[0]

   plt.figure(figsize= (10,5))
   plt.plot(Amit.index, Amit.values, color = 'blue', marker= 'o')
   plt.title("Amit and his marks")
   plt.xlabel("Subjects")
   plt.ylabel("Marks")
   plt.grid(True)
   plt.show()

def main():
   Dataf()

if __name__ == "__main__":
   main()   