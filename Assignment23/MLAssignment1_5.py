import pandas as pd

def Dataf():
   data = {'Name': ['Amit' , 'Sagar', 'Pooja'],
          'Math' : [85 , 90, 87],
          'Science' : [92 , 88, 80],
          'English' : [80 , 85 ,82]}
   
   df = pd.DataFrame(data)
   change = {'Pooja' : 'Puja'}

   df['Name'] = df['Name'].replace(change)

   print("The new data is ", df)

def main():
   Dataf()

if __name__ == "__main__":
   main()   