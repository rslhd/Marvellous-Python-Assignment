import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder

def data():
    data = {'Department' : ['HR' , 'IT' , 'Finance' , 'HR' ,'IT']}

    df = pd.DataFrame(data)
    df['Department'] = df['Department'].map({'HR' : 1, 'IT' : 2 , 'Finance' : 3})
    print("The encoded data is ",df)

def main():
    data()

if __name__ == "__main__":
    main()    