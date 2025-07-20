import pandas as pd

def Dataf():
   data = {'Name': ['Amit' , 'Sagar', 'Pooja'],
          'Math' : [85 , 90, 87],
          'Science' : [85 , 88, 80],
          'English' : [80 , 85 ,82]}
   
   df = pd.DataFrame(data)

   print("The statistical data is", df.describe())
   
def main():
   Dataf()

if __name__ == "__main__":
   main()   