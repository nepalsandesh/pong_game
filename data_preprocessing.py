import numpy as np
import pandas as pd

def left_right_direction(dataframe):
    dataset = np.array(dataframe)
    direction_list = []
    for i, row in enumerate(dataset):
        pos = row[0]
        if i==0:
            direction_list.append(0)
        else:
            print(i)
            if pos > dataset[i-1, 1]:
                direction_list.append(1)
            else:
                direction_list.append(0)
    return direction_list



def top_bottom_direction(dataframe):
    dataset = np.array(dataframe)
    direction_list = []
    for i, row in enumerate(dataset):
        pos = row[1]
        if i==0:
            direction_list.append(0)
        else:
            print(i)
            if pos > dataset[i-1, 1]:
                direction_list.append(1)
            else:
                direction_list.append(0)
    return direction_list