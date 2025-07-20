import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def data():
    data = {'Salary' : [25000, 27000, 29000, 31000, 50000, 100000]}

    money = data["Salary"]
    one  = np.percentile(money , 25)
    two = np.percentile(money, 75)

    IQR = two - one

    print("The IQR is ", IQR)
def main():
    data()

if __name__ == "__main__":
    main()    
