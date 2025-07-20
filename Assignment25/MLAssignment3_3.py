import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder

def data():
    data = {'City' : ['Pune' , 'Mumbai' , 'Delhi' , 'Pune' ,'Delhi']}

    df = pd.DataFrame(data)
    
    labelEncoder = LabelEncoder()

    df['City'] = labelEncoder.fit_transform(df['City'])
    print(df)

def main():
    data()

if __name__ == "__main__":
    main()    