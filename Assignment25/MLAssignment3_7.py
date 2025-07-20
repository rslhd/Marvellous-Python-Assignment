import pandas as pd
from sklearn.preprocessing import MinMaxScaler

def data():
    data = {'Age' : [18, 22, 25, 30, 34]}
    
    df = pd.DataFrame(data)
    scale = MinMaxScaler()

    N = ['Age']
    df[N] = scale.fit_transform(df[N])

    print("The normalize data is ", df[N])

def main():
    data()

if __name__ == "__main__":
    main()   