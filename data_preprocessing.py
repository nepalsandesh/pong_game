import numpy as np
import pandas as pd

def get_direction_list(dataframe):
    dataset = np.array(dataframe)
    direction_list = []
    for i, row in enumerate(dataset):
        pos = row[1]
        if i==0:
            direction_list.append("NaN")
        else:
            print(i)
            if pos > dataset[i-1, 1]:
                direction_list.append("positive")
            else:
                direction_list.append("negative")
    print(direction_list)
