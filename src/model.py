import numpy as np
import pandas as pd
import sklearn
from sklearn import linear_model




x =[]
y = []

model = linear_model.LinearRegression()
model.fit(x,y)



def get_position(slope, point):
    new_slope = 1 / slope * -1
    return point[1] -  (point[0]/new_slope)