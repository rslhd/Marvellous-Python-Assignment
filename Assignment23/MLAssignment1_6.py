import pandas as pd

def Dataf():
   data = {'Name': ['Amit' , 'Sagar', 'Pooja'],
          'Math' : [85 , 90, 87],
          'Science' : [92 , 88, 80],
          'English' : [80 , 85 ,82]}
   
   df = pd.DataFrame(data)
   df['Total'] = [250, 263, 249]

   Sort_df = df.sort_values(by='Total', ascending = False)

   print(Sort_df)

def main():
   Dataf()

if __name__ == "__main__":
   main()   