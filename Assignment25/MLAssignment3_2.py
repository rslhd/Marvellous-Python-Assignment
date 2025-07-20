import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def data():
    data = {'Name' : ['A', 'B', 'C'],
            'Age' : [21.0, 22.0, 23.0]}
    
    df = pd.DataFrame(data)
    
    df['Age'] = df['Age'].astype(int)

    print("The converted float to int is ", df)

def main():
    data()

if __name__ == "__main__":
    main()    