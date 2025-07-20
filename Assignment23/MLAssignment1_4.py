import pandas as pd

def Dataf():
   data = {'Name': ['Amit' , 'Sagar', 'Pooja'],
          'Math' : [85 , 90, 87],
          'Science' : [92 , 88, 80],
          'English' : [80 , 85 ,82]}
   
   df = pd.DataFrame(data)

   Marks_df = df[df['Science'] > 85]

   print("The students who got more than 85 in science is ", Marks_df )

def main():
   Dataf()

if __name__ == "__main__":
   main()   