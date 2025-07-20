import pandas as pd

def Dataf():
   data = {'Name': ['Amit' , 'Sagar', 'Pooja'],
          'Math' : [85 , 90, 87],
          'Science' : [85 , 88, 80],
          'English' : [80 , 85 ,82]}
   
   df = pd.DataFrame(data)
   print("Data is ", df)
   
   print("The total records in dataset are ", df.shape)
   print("The columns in the datasets are  ", df.head())

   print("Datatype is ", df.dtypes)

def main():
    Dataf()

if __name__ == "__main__":
    main()    
