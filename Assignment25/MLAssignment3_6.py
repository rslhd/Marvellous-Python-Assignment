import pandas as pd
from sklearn.model_selection import train_test_split

def data():
    data = {'Grade' : ['A+', 'B', 'A', 'C', 'B+']}
    
    df = pd.DataFrame(data)
    print("The data frame is ", df)

    df['Grade'] = df['Grade'].replace({'A+' : 'Execellent' , 'A' : 'Very Good', 'B+' : 'Good' , 'B' : 'Average', 'C' : 'Poor'})
    print("The new values are ", df)

def main():
    data()

if __name__ == "__main__":
    main()    